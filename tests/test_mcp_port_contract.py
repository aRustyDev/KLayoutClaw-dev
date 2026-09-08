"""Regression tests for the MCP endpoint and KLayout macro startup contract."""

import ast
import importlib.util
import json
import os
import sys
import types
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SERVER_MACRO = ROOT / "plugin" / "klayoutclaw_server.lym"
UI_MACRO = ROOT / "plugin" / "klayoutclaw_ui.lym"
DEFAULT_URL = "http://127.0.0.1:8765/mcp"
PLUGIN_URL_ARG = "${KLAYOUT_MCP_URL:-http://127.0.0.1:8765/mcp}"


def _macro_tree(path: Path) -> ast.Module:
    """Parse the actual Python payload embedded in a KLayout macro."""
    code = ET.parse(path).getroot().findtext("text")
    assert code is not None
    return ast.parse(code, filename=str(path))


def _load_module(relative_path: str, name: str):
    """Load a first-party script so its real import-time config is exercised."""
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(name, None)
    return module


def _load_server_contract(listen_ok=True):
    """Execute the server's real port resolver and constructor with fake Qt."""
    tree = _macro_tree(SERVER_MACRO)
    selected = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "DEFAULT_MCP_PORT"
            for target in node.targets
        ):
            selected.append(node)
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in {
            "_resolve_mcp_port",
            "KlayoutClawServer",
        }:
            selected.append(node)

    callback_state = types.SimpleNamespace(
        on_request=None,
        on_server_start=None,
        on_error=None,
        server_port=None,
        startup_error=None,
    )
    log = []

    class FakeTcpServer:
        def __init__(self, parent=None):
            self.parent = parent
            self.listen_calls = []
            self.connection_callback = None

        def listen(self, address, port):
            self.listen_calls.append((address, port))
            return listen_ok

        def newConnection(self, callback):
            self.connection_callback = callback

    fake_pya = types.SimpleNamespace(
        QTcpServer=FakeTcpServer,
        QHostAddress=lambda address: address,
    )
    namespace = {
        "os": os,
        "sys": types.SimpleNamespace(modules={"_klayoutclaw": callback_state}),
        "pya": fake_pya,
        "_log": log.append,
    }
    module = ast.Module(body=selected, type_ignores=[])
    exec(compile(module, str(SERVER_MACRO), "exec"), namespace)
    return namespace, callback_state, log


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (None, 8765),
        ("1", 1),
        ("8766", 8766),
        ("65535", 65535),
    ],
)
def test_actual_server_macro_resolves_valid_ports(raw, expected):
    namespace, _, _ = _load_server_contract()
    env = {} if raw is None else {"KLAYOUT_MCP_PORT": raw}
    assert namespace["_resolve_mcp_port"](env) == expected


@pytest.mark.parametrize("raw", ["", "abc", "0", "-1", "65536"])
def test_actual_server_macro_rejects_invalid_ports(raw):
    namespace, _, _ = _load_server_contract()
    with pytest.raises(ValueError, match="KLAYOUT_MCP_PORT"):
        namespace["_resolve_mcp_port"]({"KLAYOUT_MCP_PORT": raw})


def test_actual_server_macro_publishes_successful_port(monkeypatch):
    namespace, callback_state, log = _load_server_contract(listen_ok=True)
    monkeypatch.setenv("KLAYOUT_MCP_PORT", "8766")

    server = namespace["KlayoutClawServer"]()

    assert server.started is True
    assert server.port == 8766
    assert server.listen_calls == [("127.0.0.1", 8766)]
    assert callback_state.server_port == 8766
    assert callback_state.startup_error is None
    assert any("127.0.0.1:8766" in line for line in log)


def test_actual_server_macro_persists_bind_failure(monkeypatch):
    namespace, callback_state, log = _load_server_contract(listen_ok=False)
    monkeypatch.setenv("KLAYOUT_MCP_PORT", "8766")

    server = namespace["KlayoutClawServer"]()

    assert server.started is False
    assert server.port is None
    assert callback_state.server_port is None
    assert "127.0.0.1:8766" in callback_state.startup_error
    assert "port may be in use" in callback_state.startup_error
    assert log[-1] == callback_state.startup_error


def test_actual_server_macro_persists_invalid_port_failure(monkeypatch):
    namespace, callback_state, log = _load_server_contract(listen_ok=True)
    monkeypatch.setenv("KLAYOUT_MCP_PORT", "not-a-port")

    server = namespace["KlayoutClawServer"]()

    assert server.started is False
    assert server.listen_calls == []
    assert callback_state.server_port is None
    assert "KLAYOUT_MCP_PORT" in callback_state.startup_error
    assert log[-1] == callback_state.startup_error


def test_ui_macro_uses_callback_port_and_persisted_startup_error():
    code = ET.parse(UI_MACRO).getroot().findtext("text")
    assert code is not None
    assert 'getattr(cb, "startup_error", None)' in code

    tree = ast.parse(code, filename=str(UI_MACRO))
    selected = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name in {
            "_set_status_running",
            "_on_server_start",
            "_on_error",
        }
    ]

    class FakeLabel:
        def __init__(self):
            self.text = None
            self.style = None

        def setText(self, value):
            self.text = value

        def setStyleSheet(self, value):
            self.style = value

    class FakeTimer:
        def __init__(self):
            self.started = []
            self.stops = 0

        def start(self, delay):
            self.started.append(delay)

        def stop(self):
            self.stops += 1

    callback_state = types.SimpleNamespace(server_port=None, startup_error="bind failed")
    label = FakeLabel()
    timer = FakeTimer()
    log = []
    namespace = {
        "sys": types.SimpleNamespace(modules={"_klayoutclaw": callback_state}),
        "datetime": __import__("datetime"),
        "_ui_status": label,
        "_ui_timer": timer,
        "_append_log": lambda text, success: log.append((text, success)),
    }
    exec(
        compile(ast.Module(body=selected, type_ignores=[]), str(UI_MACRO), "exec"),
        namespace,
    )

    namespace["_on_error"]("bind failed")
    assert label.text == "MCP: Error \u25cf"
    assert timer.started == []

    namespace["_on_server_start"](8766)
    assert label.text == "MCP: Running \u25cf :8766"
    assert callback_state.startup_error is None

    namespace["_on_error"]("transient request failure")
    assert timer.started == [5000]


def test_active_default_endpoint_contract():
    """First-party defaults stay on 8765 while runtime overrides remain possible."""
    direct = json.loads((ROOT / "mcp_config.json").read_text())
    assert direct["mcpServers"]["klayoutclaw"]["url"] == DEFAULT_URL

    proxy = json.loads((ROOT / ".mcp.json").read_text())
    assert proxy["mcpServers"]["klayoutclaw"]["args"][1] == PLUGIN_URL_ARG

    skills_dir = ROOT / "skills" / "scripts"
    sys.path.insert(0, str(skills_dir))
    try:
        import mcp_client

        assert mcp_client._DEFAULT_URL == DEFAULT_URL
    finally:
        sys.path.remove(str(skills_dir))

    config_source = (ROOT / "agent" / "src" / "config.ts").read_text()
    assert config_source.count(
        'process.env.KLAYOUT_MCP_URL ?? "http://127.0.0.1:8765/mcp"'
    ) == 2

    agent_source = (ROOT / "agent" / "src" / "agent.ts").read_text()
    assert "KLayout MCP ${config.klayout.url}" in agent_source
    assert 'connectedServers.push("klayout (KLayout MCP :8765)")' not in agent_source


@pytest.mark.parametrize(
    ("relative_path", "attribute"),
    [
        ("tools/capture_demo.py", "MCP_URL"),
        ("tools/capture_ml08_demo.py", "MCP_URL"),
        ("skills/e2e_judge/scripts/harness.py", "KLAYOUT_MCP_URL"),
        ("skills/e2e_judge/scripts/verifier.py", "KLAYOUT_URL"),
    ],
)
def test_active_python_clients_honor_url_override(
    monkeypatch, relative_path, attribute
):
    override = "http://127.0.0.1:8766/mcp"
    monkeypatch.setenv("KLAYOUT_MCP_URL", override)

    module = _load_module(relative_path, "_port_contract_" + attribute)

    assert getattr(module, attribute) == override


def test_shared_client_reads_actual_plugin_config(monkeypatch):
    monkeypatch.delenv("KLAYOUT_MCP_URL", raising=False)
    client = _load_module(
        "skills/scripts/mcp_client.py", "_port_contract_mcp_client"
    )

    assert client.load_mcp_config(str(ROOT / ".mcp.json")) == DEFAULT_URL

    override = "http://127.0.0.1:8766/mcp"
    monkeypatch.setenv("KLAYOUT_MCP_URL", override)
    assert client.load_mcp_config(str(ROOT / ".mcp.json")) == override


def test_e2e_judge_passes_url_override_to_claude(monkeypatch):
    override = "http://127.0.0.1:8766/mcp"
    monkeypatch.setenv("KLAYOUT_MCP_URL", override)
    harness = _load_module(
        "skills/e2e_judge/scripts/harness.py", "_port_contract_harness"
    )
    observed = {}

    def fake_run(cmd, **kwargs):
        observed["cmd"] = cmd
        return types.SimpleNamespace(stdout="ok", stderr="", returncode=0)

    monkeypatch.setattr(harness.subprocess, "run", fake_run)
    result = harness.run_agent("probe", agent="claude")

    config_arg = observed["cmd"][observed["cmd"].index("--mcp-config") + 1]
    config = json.loads(config_arg)
    assert config["mcpServers"]["klayoutclaw"]["url"] == override
    assert result.success
