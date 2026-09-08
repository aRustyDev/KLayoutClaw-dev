"""Safe lifecycle management for files copied into KLayout's macro home."""

from __future__ import annotations

import hashlib
import importlib.resources
import json
import os
import platform
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

from ._version import __version__

INSTALL_MANIFEST = ".klayoutclaw-install.json"
RUNTIME_CONFIG = "klayoutclaw-runtime.json"
WORKER_IMPORTS = ("gdstk", "klayout", "numpy", "shapely", "skimage")


class LifecycleError(RuntimeError):
    """Raised when an operation cannot safely alter an installation."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _file_hash(path: Path) -> str:
    return _sha256(path.read_bytes())


def default_target_dir(environ: dict[str, str] | None = None) -> Path:
    """Return KLayout's user ``pymacros`` directory.

    ``KLAYOUT_HOME`` denotes KLayout's user home, so its ``pymacros`` child is
    used. ``--target-dir`` bypasses this helper and denotes ``pymacros`` itself.
    """
    env = os.environ if environ is None else environ
    configured_home = env.get("KLAYOUT_HOME")
    if configured_home:
        return Path(configured_home).expanduser() / "pymacros"
    return Path.home() / ".klayout" / "pymacros"


def _safe_relative(value: str) -> Path:
    pure = PurePosixPath(value)
    if pure.is_absolute() or not pure.parts or ".." in pure.parts:
        raise LifecycleError(f"unsafe path in installation manifest: {value!r}")
    return Path(*pure.parts)


def _payload_root():
    return importlib.resources.files("klayoutclaw.payload")


def payload_manifest() -> dict[str, Any]:
    data = json.loads(
        _payload_root().joinpath("manifest.json").read_text(encoding="utf-8")
    )
    if data.get("schema") != 1:
        raise LifecycleError("unsupported packaged payload manifest schema")
    if data.get("version") != __version__:
        raise LifecycleError(
            "packaged payload version does not match the distribution version"
        )
    return data


def payload_files() -> dict[str, bytes]:
    """Return destination-relative payload bytes, validating every digest."""
    result: dict[str, bytes] = {}
    for entry in payload_manifest().get("files", []):
        destination = _safe_relative(entry["destination"]).as_posix()
        resource = _safe_relative(entry["resource"])
        data = _payload_root().joinpath(*resource.parts).read_bytes()
        if _sha256(data) != entry.get("sha256"):
            raise LifecycleError(f"packaged payload digest mismatch: {resource}")
        if destination in result:
            raise LifecycleError(f"duplicate payload destination: {destination}")
        result[destination] = data
    return result


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise LifecycleError(f"cannot read {path.name}: {exc}") from exc
    if not isinstance(data, dict):
        raise LifecycleError(f"{path.name} must contain a JSON object")
    return data


def _owned_files(manifest: dict[str, Any] | None) -> dict[str, str]:
    if manifest is None:
        return {}
    if manifest.get("schema") != 1:
        raise LifecycleError("unsupported installation manifest schema")
    result = {}
    for entry in manifest.get("files", []):
        relative = _safe_relative(entry["path"]).as_posix()
        digest = entry.get("sha256")
        if not isinstance(digest, str):
            raise LifecycleError(f"missing digest for owned file: {relative}")
        result[relative] = digest
    return result


def _runtime_bytes(existing: dict[str, Any] | None = None) -> bytes:
    installed_at = _utc_now()
    if existing:
        same_runtime = (
            existing.get("schema") == 1
            and existing.get("plugin_version") == __version__
            and existing.get("worker_python") == sys.executable
        )
        if same_runtime and isinstance(existing.get("installed_at"), str):
            installed_at = existing["installed_at"]
    config = {
        "schema": 1,
        "plugin_version": __version__,
        "worker_python": sys.executable,
        "installed_at": installed_at,
    }
    return (json.dumps(config, indent=2, sort_keys=True) + "\n").encode()


def _desired_files(target: Path) -> dict[str, bytes]:
    desired = payload_files()
    runtime = None
    runtime_path = target / RUNTIME_CONFIG
    try:
        runtime = _read_json(runtime_path)
    except LifecycleError:
        # A malformed runtime file is treated as a modified destination during
        # preflight; the desired replacement can still be computed safely.
        pass
    desired[RUNTIME_CONFIG] = _runtime_bytes(runtime)
    return desired


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", prefix=f".{path.name}.", dir=path.parent, delete=False
        ) as handle:
            temporary = handle.name
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, 0o644)
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            try:
                Path(temporary).unlink()
            except FileNotFoundError:
                pass


def _current_hash(path: Path) -> str | None:
    return _file_hash(path) if path.is_file() else None


def _reject_symlink_parents(target: Path, relative: str) -> None:
    current = target
    for part in _safe_relative(relative).parts[:-1]:
        current /= part
        if current.is_symlink():
            raise LifecycleError(
                f"refusing to traverse symlinked installation directory: {current}"
            )


def _preflight(
    target: Path,
    desired: dict[str, bytes],
    owned: dict[str, str],
) -> tuple[list[str], list[str], list[str]]:
    writes: list[str] = []
    removals: list[str] = []
    conflicts: list[str] = []

    desired_hashes = {path: _sha256(data) for path, data in desired.items()}
    for relative, digest in desired_hashes.items():
        _reject_symlink_parents(target, relative)
        path = target / _safe_relative(relative)
        current = _current_hash(path)
        if current == digest:
            continue
        writes.append(relative)
        previous = owned.get(relative)
        if (path.exists() and current is None) or (
            current is not None and (previous is None or current != previous)
        ):
            conflicts.append(relative)

    for relative, previous in owned.items():
        _reject_symlink_parents(target, relative)
        if relative in desired:
            continue
        path = target / _safe_relative(relative)
        current = _current_hash(path)
        if current is None:
            continue
        removals.append(relative)
        if current != previous:
            conflicts.append(relative)

    return sorted(writes), sorted(removals), sorted(set(conflicts))


def install(
    target_dir: str | os.PathLike[str] | None = None,
    *,
    force: bool = False,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Install the packaged payload without overwriting local changes."""
    target = Path(target_dir) if target_dir is not None else default_target_dir()
    target = target.expanduser().resolve()
    manifest_path = target / INSTALL_MANIFEST

    try:
        previous_manifest = _read_json(manifest_path)
        owned = _owned_files(previous_manifest)
    except LifecycleError:
        if not force:
            raise
        previous_manifest = None
        owned = {}

    desired = _desired_files(target)
    writes, removals, conflicts = _preflight(target, desired, owned)
    if conflicts and not force:
        joined = ", ".join(conflicts)
        raise LifecycleError(
            f"refusing to replace locally modified or unowned files: {joined}; "
            "rerun with --force to replace only these exact destinations"
        )

    current_version = previous_manifest and previous_manifest.get("version")
    manifest_current = (
        previous_manifest is not None
        and current_version == __version__
        and set(owned) == set(desired)
        and all(owned[path] == _sha256(data) for path, data in desired.items())
    )
    if not writes and not removals and manifest_current:
        return {
            "status": "current",
            "target": str(target),
            "version": __version__,
            "changed": False,
            "dry_run": dry_run,
            "written": [],
            "removed": [],
        }

    if dry_run:
        return {
            "status": "would-install",
            "target": str(target),
            "version": __version__,
            "changed": bool(writes or removals or not manifest_current),
            "dry_run": True,
            "written": writes,
            "removed": removals,
        }

    existing_dirs = set()
    for relative in desired:
        parent = (target / _safe_relative(relative)).parent
        while parent != target and target in parent.parents:
            if parent.exists():
                existing_dirs.add(parent)
            parent = parent.parent

    target.mkdir(parents=True, exist_ok=True)
    for relative in writes:
        _atomic_write(target / _safe_relative(relative), desired[relative])
    for relative in removals:
        try:
            (target / _safe_relative(relative)).unlink()
        except FileNotFoundError:
            pass

    previous_created = (
        [] if previous_manifest is None else previous_manifest.get("created_dirs", [])
    )
    created_dirs = {_safe_relative(value).as_posix() for value in previous_created}
    for relative in desired:
        parent = (target / _safe_relative(relative)).parent
        while parent != target and target in parent.parents:
            if parent not in existing_dirs:
                created_dirs.add(parent.relative_to(target).as_posix())
            parent = parent.parent

    now = _utc_now()
    first_installed = now
    if previous_manifest and isinstance(previous_manifest.get("installed_at"), str):
        first_installed = previous_manifest["installed_at"]
    installed_manifest = {
        "schema": 1,
        "version": __version__,
        "installed_at": first_installed,
        "updated_at": now,
        "created_dirs": sorted(created_dirs),
        "files": [
            {"path": relative, "sha256": _sha256(desired[relative])}
            for relative in sorted(desired)
        ],
    }
    _atomic_write(
        manifest_path,
        (json.dumps(installed_manifest, indent=2, sort_keys=True) + "\n").encode(),
    )
    return {
        "status": "installed",
        "target": str(target),
        "version": __version__,
        "changed": True,
        "dry_run": False,
        "written": writes,
        "removed": removals,
    }


def status(target_dir: str | os.PathLike[str] | None = None) -> dict[str, Any]:
    """Inspect the installed copy without changing the filesystem."""
    target = Path(target_dir) if target_dir is not None else default_target_dir()
    target = target.expanduser().resolve()
    manifest_path = target / INSTALL_MANIFEST
    try:
        manifest = _read_json(manifest_path)
        owned = _owned_files(manifest)
    except LifecycleError as exc:
        return {
            "status": "invalid-manifest",
            "target": str(target),
            "version": __version__,
            "error": str(exc),
            "files": [],
        }

    if manifest is None:
        return {
            "status": "not-installed",
            "target": str(target),
            "version": __version__,
            "files": [],
        }

    desired = _desired_files(target)
    desired_hashes = {path: _sha256(data) for path, data in desired.items()}
    file_states = []
    for relative in sorted(set(owned) | set(desired_hashes)):
        current = _current_hash(target / _safe_relative(relative))
        installed_hash = owned.get(relative)
        expected_hash = desired_hashes.get(relative)
        if current is None:
            state = "missing"
        elif installed_hash is None:
            state = "stale"
        elif current != installed_hash:
            state = "modified"
        elif expected_hash != installed_hash:
            state = "stale"
        else:
            state = "current"
        file_states.append({"path": relative, "status": state})

    states = {entry["status"] for entry in file_states}
    if "modified" in states:
        overall = "modified"
    elif "missing" in states:
        overall = "missing"
    elif manifest.get("version") != __version__:
        overall = "version-mismatched"
    elif "stale" in states:
        overall = "stale"
    else:
        overall = "current"
    return {
        "status": overall,
        "target": str(target),
        "version": __version__,
        "installed_version": manifest.get("version"),
        "files": file_states,
    }


def _remove_empty_owned_dirs(target: Path, manifest: dict[str, Any]) -> None:
    directories = []
    for relative in manifest.get("created_dirs", []):
        path = target / _safe_relative(relative)
        directories.append(path)
    for path in sorted(directories, key=lambda item: len(item.parts), reverse=True):
        try:
            path.rmdir()
        except (FileNotFoundError, OSError):
            pass


def uninstall(
    target_dir: str | os.PathLike[str] | None = None,
    *,
    force: bool = False,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Remove only files recorded in KlayoutClaw's ownership manifest."""
    target = Path(target_dir) if target_dir is not None else default_target_dir()
    target = target.expanduser().resolve()
    manifest_path = target / INSTALL_MANIFEST
    manifest = _read_json(manifest_path)
    if manifest is None:
        return {
            "status": "not-installed",
            "target": str(target),
            "changed": False,
            "dry_run": dry_run,
            "removed": [],
        }
    owned = _owned_files(manifest)
    modified = []
    present = []
    for relative, installed_hash in owned.items():
        _reject_symlink_parents(target, relative)
        path = target / _safe_relative(relative)
        current = _current_hash(path)
        if current is None:
            continue
        present.append(relative)
        if current != installed_hash:
            modified.append(relative)
    if modified and not force:
        raise LifecycleError(
            "refusing to remove locally modified files: "
            + ", ".join(sorted(modified))
            + "; rerun with --force to remove only these recorded files"
        )
    removed = sorted(present)
    if dry_run:
        return {
            "status": "would-uninstall",
            "target": str(target),
            "changed": True,
            "dry_run": True,
            "removed": removed,
        }
    for relative in removed:
        try:
            (target / _safe_relative(relative)).unlink()
        except FileNotFoundError:
            pass
    try:
        manifest_path.unlink()
    except FileNotFoundError:
        pass
    _remove_empty_owned_dirs(target, manifest)
    return {
        "status": "uninstalled",
        "target": str(target),
        "changed": True,
        "dry_run": False,
        "removed": removed,
    }


def _probe_worker_imports(interpreter: Path) -> dict[str, bool]:
    probe = (
        "import importlib.util,json; "
        f"names={list(WORKER_IMPORTS)!r}; "
        "print(json.dumps({name: importlib.util.find_spec(name) is not None for name in names}))"
    )
    completed = subprocess.run(
        [str(interpreter), "-c", probe],
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    if completed.returncode != 0:
        return {name: False for name in WORKER_IMPORTS}
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError:
        return {name: False for name in WORKER_IMPORTS}
    return {name: bool(result.get(name)) for name in WORKER_IMPORTS}


def doctor(target_dir: str | os.PathLike[str] | None = None) -> dict[str, Any]:
    """Diagnose the core installation and optional worker environment."""
    target = Path(target_dir) if target_dir is not None else default_target_dir()
    target = target.expanduser().resolve()
    installation = status(target)
    runtime_path = target / RUNTIME_CONFIG
    runtime: dict[str, Any] | None = None
    runtime_error = None
    try:
        runtime = _read_json(runtime_path)
    except LifecycleError as exc:
        runtime_error = str(exc)

    worker_python = None if runtime is None else runtime.get("worker_python")
    interpreter = Path(worker_python) if isinstance(worker_python, str) else None
    interpreter_exists = bool(interpreter and interpreter.is_file())
    imports = (
        _probe_worker_imports(interpreter)
        if interpreter is not None and interpreter_exists
        else {name: False for name in WORKER_IMPORTS}
    )
    if not interpreter_exists:
        worker_status = "interpreter-missing"
    elif all(imports.values()):
        worker_status = "available"
    else:
        worker_status = "dependencies-missing"
    return {
        "status": "ok" if installation["status"] == "current" else "problems-found",
        "platform": platform.platform(),
        "installation": installation,
        "runtime_error": runtime_error,
        "workers": {
            "status": worker_status,
            "python": worker_python,
            "imports": imports,
        },
    }
