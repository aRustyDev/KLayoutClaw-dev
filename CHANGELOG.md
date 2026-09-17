# Changelog

All notable changes to KlayoutClaw are documented here. This file is generated
from the repository's Conventional Commit history by git-cliff.

## 0.6.0 - 2026-09-17

### Bug fixes

- Align MCP handler field names with route_worker.py (`e2cb587`)

- Pin exclusion zones + rasterization API fix (`bb3f461`)

- UTF-8 compatibility in stdio logging (`2a1a7db`)

- Update find_path for negative sentinel cost convention (`4ff0a06`)

- Restore pin exclusion corridors in obstacle region (`fc215f0`)

- Snap path endpoints to exact pin coordinates (`5042abe`)

- _refresh_view no longer overrides user zoom_box() (`f228830`)

- Evaluate_design MCP tool parameter exposure and handler bug (`ebcf33e`)

- Rewrite bottom_hbn detection to use bottom_part + SIFT warp (`1b3cbdb`)

- Resolve 8 GitHub issues — stale handles, eval worker, agent wrappers, server features (`071053f`)

- Improve auto_route error feedback for empty pin layers (`3e04bff`)

- Remove redundant detect_stack orchestrator tool (`f1f22fb`)

- Resolve gdsalign commit + get_layout_info crashes, warp orientation (`3e0092d`)

- Thinking-only termination guard + stdio-via-mcp-remote URL parsing (`5a9f264`)

- **evaluate:** Drop graphene/graphite defaults from bulk_containment (`016fbbe`)

- **route_inspect:** Require contact_layers + pad_layer explicitly (`6e4083e`)

- **route_inspect:** Reject empty contact_layers; test cleanups (`f7468b7`)

- **evaluate:** Strip Hall-bar vocabulary from next_step_suggestion (`77185d8`)

- **schema:** Remove Hall-bar layer_map example from evaluate_design (`5b87bdd`)

- **e2e:** Drop tmux; portable background+poll timeout (`67a1fce`)

- **e2e:** Route_override verifies via MCP query, not response.paths (`fc682cf`)

- **e2e:** Execute_script response shape — result dict merged at top-level (`d46618c`)

- **e2e:** Don't assert on absent 'status' key in execute_script response (`484d6cd`)

- **plugin/vc:** RB-4 optional layout arg for spec-compliant dirty detection (`3fe824c`)

- **plugin/vc:** RB-2 atomicity on first-checkpoint failure (`3e2ee0a`)

- **plugin/vc:** DM-3 preserve SREF/AREF instance properties in to_pya_code (`9aab21d`)

- **plugin/vc:** RB-4 cache layout weakref for no-arg status() dirty detection (`c76c533`)

- **agent/tui:** Propagate think_recorded source through reducer → AssistantMessage (TH-6/TH-9/T38 live path) (`db09f62`)

- **agent/tools:** Exempt thinking from disabledTools filter (TH-4 always-listed invariant) (`c446c65`)

- **agent/planning:** Preserve legacy exit tool compatibility (`2cb8fe6`)

- **agent/history:** Clear dangling latest symlink before recreate (prod bug flagged by G4) (`f6459cb`)

- **agent/subagent:** Resolve delegate crash + redesign API (issue #23) (`8d92637`)

- **agent/tui:** Delegate placeholder reads new schema field names (finding #1) (`b4f71fd`)

- **agent/subagent:** Config role overrides built-in 'general-purpose' (finding #2) (`fbb1855`)

- **agent/subagent:** Emit started+completed from model-resolution error (finding #3) (`9966436`)

- **agent/tools:** Delegate catalog uses effective general-purpose role (R2 finding #1) (`aa9f9a0`)

- **agent/tui:** Placeholder shows effective role via resolver (R2 finding #2) (`3180b35`)

- **agent:** Register delegate on subagent.enabled regardless of role count (R3 finding #1) (`c813521`)

- **agent:** Clear TUI placeholder on delegate validation failure (R3 finding #2) (`4129347`)

- **agent/tools:** Delegate schema descriptions surface runtime contract (R4 finding #1) (`c8c4490`)

- **agent/prompts:** Delegation section uses effective general-purpose role (R4 finding #2) (`0c32d01`)

- **agent/tools:** Carve delegate out of plan_drafted freeze wrapper (R5 finding #1) (`3116fce`)

- **agent/tools:** Defer delegate emitCancelled to next microtask (R6 finding #1) (`dd0de64`)

- **plan-reinjector:** Insert reminder before terminal user message (Finding 1) (`1ddafec`)

- **plan-reinjector:** Skip reinjection for abandoned/completed plans (Finding 2) (`2472cf0`)

- **tui:** Intercept /plan status in App.tsx before plan creation (Finding 3) (`4fb7ae9`)

- **plan-reinjector:** Bump turn counter BEFORE prompt, not after (R2 finding #1) (`f214814`)

- **#24:** R2 finding #2 — CLI /plan commands now work in plain mode (`ce21bb5`)

- **#24:** R3 finding #1 — roll back pre-prompt bump on failed turns (`00be8bf`)

- **#24:** R3 finding #2 — close auto-executed plans as completed (`3f85e44`)

- **#24:** R3 finding #3 — route /plan verify through the user (`bc96e0e`)

- **#24:** R4 finding #1 — per-user-turn latch for plan reinjection (`c7b43bf`)

- **#24:** R4 finding #2 — pruner keys on sentinel, not substring (`fc64330`)

- **#24:** R5 finding #1 (gpt-5.5 xhigh) — roll back on swallowed errors (`f47cbde`)

- **agent/cli:** Robust thinking-only termination detection (issue #22) (`a562ca8`)

- **agent/cli:** Detect stopReason=error and stalled toolUse terminations (`b48b062`)

- **agent:** Reset buffered output on retry (review finding #1) (`0e822f8`)

- **agent:** Distinguish refusals from transport errors (review finding #3) (`1f70493`)

- **agent:** Gate error-retry on errorMessage, not content (R2 finding #1) (`a536d4a`)

- **agent:** Activity fallback only fires when no terminal assistant (R2 finding #2) (`2d1c529`)

- **agent:** Exclude non-retryable errors from retry gate (R3 finding #1) (`bba1126`)

- **agent:** Surface exhausted retries as error, not false success (R3 finding #2) (`22c64a5`)

- **agent:** Drop stalled-toolUse retry — Continue-prompt corrupts tool state (R4 finding #1) (`7d35f74`)

- **agent:** Emit terminal thinking_only_reset on RPC exhaustion (R4 finding #2) (`b9ba519`)

- **agent:** Set exitCode and return instead of process.exit on JSON error (R5 finding #1) (`d4eda27`)

- **agent:** Disable activity fallback — pi extensions can resolve prompt() cleanly (R7 finding #1 gpt-5.5 xhigh verification) (`e19b5bc`)

- **agent:** Surface non-retryable provider errors as terminal, not silent success (R8 finding #1) (`680cde0`)

- **agent:** Bound guard scans to current prompt's messages (R8 finding #2) (`2b5339e`)

- **tests:** Early return in exhaustion test skipped all assertions (R8 finding #3) (`8f19f4a`)

- **agent:** Rebind sinceIdx when pi-coding-agent compacts mid-prompt (R8 final) (`e0dfb4a`)

- **agent:** Check context overflow before retryable regex in terminal helper (`9cd0a30`)

- **agent:** Track sinceIdx by message identity, not length (R8.3 final) (`c8dbb7a`)

- **agent:** \b-bound HTTP status codes in retryable regex (R8.4 final) (`3343cfa`)

- **detect:** #27 candidate D1 — best-per-material consolidation; 29/40 cells, 2 stacks all-pass (`a4e25d1`)

- **route:** #28 ordered-loop pairing + freeze + bus_pairs (C3 hybrid) (`a7beedc`)

- #31 reuse precomputed SIFT warp via --warp PATH (`0cef808`)

- #33 per-stage diagnostics + --min-area in combine.transform (`7dc1697`)

- #25 strip vc_* tools from _TOOL_DISPATCH (`1ff7e40`)

- #36 prepend PLANNER, NOT EXECUTOR on planner tool descriptions (`11203c2`)

- **flakedetect:** Invert SIFT warp before diff in footprint.py (`d3eb4bd`)

- **test:** Gt_evaluator pixel_size default 0.106→0.087 (`950284f`)

- **detect:** Graphite.py — dark-strip rescue so thin strips reach the pool (`d60845d`)

- **harness:** Make evaluate_design usable — object-param schema, arm_material_class forms, false-zero (`65a9b29`)

- **gdsalign:** HM11 rotation-branch floor + registration self-validation gate (`e52b468`)

- **harness+skills:** Atomic save-best, ping liveness probe, frame contract, graphene-warp check (`9acac92`)

- **review:** Address adversarial verification findings (`66c933c`)

- **review2:** Address critical re-verification findings (save-best, frame fallback, test quality) (`2d3fcb4`)

- **route_material_compat:** Error (not false 0.0) when material layers absent (`b0ee03b`)

- **e2e:** Material-containment guard — contacts/arm-tips must stay on the flake (`68f4368`)

- **flakedetect:** Improve source diff alignment (`008189f`)

- **align:** Preserve legacy target options (`5743ff5`)

- Make MCP endpoint startup and detection truthful (`960d7ff`)

- Propagate MCP URL override to all clients (`85e72d8`)

- Harden uv packaging lifecycle validation (`324a73f`)

- Launch plugin MCP proxy with resolved URL (`9f91d9e`)

- Avoid Desktop MCP placeholder expansion (`add39d8`)

- Install release test dependencies (`9a7182d`)


### Documentation

- Add auto_route documentation and update project files (`2579641`)

- Mark v0.5 autorouter verification complete (`c6a0297`)

- Add demo GIF, DEVELOPMENT.md, and device physics description (`286820b`)

- Add route_worker.py quality enhancement design spec (`4ebc24c`)

- Add route_worker quality enhancement implementation plan (`cc78241`)

- Update auto_route tool reference for graduated damping (`102da28`)

- Acknowledge Klayout-Router for routing algorithm techniques (`6027209`)

- Add ML08 nanodevice demo to README (`64d5bce`)

- Qlaybot v0.4.1 — specs, plans, workspace knowledge, and project docs (`e66f459`)

- Qlaybot v0.4.1 — Codex quality review report (`893c28f`)

- Spec for OpenAI-compatible provider support in qlaybot (`3658c92`)

- Update for generalized e2e design and evaluate_design (`3763788`)

- Strip Hall-bar defaults from tools.md + CLAUDE.md (`2c8c0de`)

- **skill:** Generalize rank_candidate_pairs framing (`6a5ad4e`)

- Document material_overlap_report primitive (`d7ab419`)

- Document pin_pairs_override workflow (`a5fab4a`)

- **plan:** 2026-04-17 benchmark review fixes plan (`db495dd`)

- Update report for 2026-04-14/15 benchmark review fixes (`f58dc2a`)

- Sync README/CLAUDE/skills with post-benchmark-review state + new logo & demo video (`6826aa5`)

- **scripts:** Normalize flakedetect script docstrings to conda env instrMCPdev (`a28d018`)

- **readme:** Use GitHub user-attachments URL for E2E demo video (`fb82c61`)

- **readme:** Point Demo.mp4 embed at demo-assets release (`c719a5e`)

- **readme:** Use user-attachments URL for compressed Demo video (`af5c41f`)

- **readme:** Rewrite Qlaybot section to match v0.4.2 codebase (`d46fa6e`)

- **assets:** Recompress Demo.mp4 (13MB → 9MB) (`f855cc5`)

- **specs:** Add qlaybot v0.4.3 design (plan mode + image + truncate + verbose) (`fd5cc64`)

- **specs:** Qlaybot v0.4.3 design v2 — address Codex review findings (`b703dad`)

- **specs:** Qlaybot v0.4.3 design v3 — address Codex second-pass findings (`1568a95`)

- **specs:** Qlaybot v0.4.3 design v3.1 — incorporate Group 1 findings (`458f6bd`)

- **plans:** Qlaybot v0.4.4 implementation plan (`21710a1`)

- **CLAUDE.md:** Update MCP tool count to 19 for Phase 5 additions (`a01b7cb`)

- **plans:** Tighten v0.4.4 Phase 8 gate (`f77b123`)

- **release:** V0.4.4 manual E2E guide + gitignore + route_worker dry-run (`9a7f2a9`)

- **readme:** Rewrite as concise scan-first landing page (`9465fc8`)

- Plans for qlaybot issues #22, #23, #24 + early-exit report (`281c5cf`)

- **reviews:** Archive #23/#24 review chains + pre-existing test-failures doc (`5e04464`)

- **agent:** Finding #2 investigation — fallback is theoretical-only (`84f8a1c`)

- Response report for code-review issue #22 pass (`bc59403`)

- **reviews:** Archive #22 review chain (8 rounds + 4 follow-ups) (`696d5ca`)

- #35 execute_script import availability (`211b3df`)

- #37 KLayout restart recovery procedure (`d1a0f1a`)

- Align surface area with ordered-loop assignment + nanodevice DRC framing (`2b67c80`)

- Add detector de-tuning TRD plan (8 phases) (`fe2c636`)

- Revise plan to use GT evaluator as regression gate (`1864ea8`)

- **detect:** Held-out montage on 13 AH/HM/QH fixtures (Phase 8) (`3d60d8b`)

- **detect:** Failure prioritization report for 0.8 gate (`7975cc8`)

- **detect:** Phase 10 progress report (2026-05-21) (`f87bdd0`)

- **detect:** Phase 11 progress report — composite scoring Step A results (`dee7cb8`)

- **detect:** Phase 13 results — footprint grow + flood_fill diagnosis (`f450eac`)

- **detect:** Graphite Phase 17 — irreducibility diagnosis for AH06/QH07/HM06 (`c598ce2`)

- **detect:** Phase 18 pixel_size audit — purely cosmetic mismatch, no change (`346c739`)

- **detect:** Comprehensive final report (Phases 0-19) (`fa5832a`)

- **e2e:** Tell the agent to run route_material_compat after routing (`cf5f067`)

- **qb-opus48:** Add feedback-fix + two-level report and triage verdicts (`b570f00`)

- Explain paired MCP port overrides (`ee3d0d7`)

- Explain merge-gate bootstrap order (`1dc9858`)


### Features

- Add route_worker.py subprocess routing engine (`7dffbd3`)

- Add auto_route MCP tool (v0.5) (`7b5c343`)

- **nanodevice:flakedetect:** Add vdW heterostructure stack detection skill (`5bae730`)

- **nanodevice:gdsalign:** Add GDS template alignment skill (`03cb74a`)

- Add graduated damping helpers and cost grid builder (`76f6c62`)

- Add pin-aware cost field, per-pair recovery, sorted routing (`e844920`)

- Expose key routing tuning params in MCP auto_route schema (`67e359b`)

- ML08 Hall bar demo with multi-window routing (`df177ca`)

- Qlaybot v0.4.1 — agent, autonomous pipeline, MCP server, and skills (`1371f11`)

- Support OpenAI-compatible providers in qlaybot (`771c7ea`)

- Update evaluate_design MCP tool for configurable checks (`51be41f`)

- Rewrite nanodevice_e2e_design as device-agnostic methodology (`3fd4bee`)

- Generalize skills and e2e tests for device-agnostic evaluate_design (`3477dc6`)

- Generalize qlaybot workspace docs for device-agnostic design (`86cac1d`)

- Add diff-mode footprint detection and cluster splitting (`e89fd18`)

- Rewrite nanodevice tool registrations to match current skill set (`09e21a4`)

- Qlaybot agent flush thinking before tool calls, env var model override (`0f805ea`)

- **evaluate:** Add material_overlap_report primitive (`dc2f36e`)

- **mcp:** Register material_overlap_report primitive in schema (`2b450ff`)

- **route:** Add pin_pairs_override to auto_route (`c350b41`)

- **mcp:** Expose pin_pairs_override in auto_route schema (`4e7d97e`)

- Qlaybot v0.4.3 — Plan Mode + iTerm2 image render + transcript truncation + --verbose (`f4fa771`)

- Klayout git first doc. (`ec73297`)

- **agent/events:** Add TranscriptMarkerEmitter (v0.4.4 §4.7 producer) (`4b6fc78`)

- **agent/events:** Add get/setTranscriptMarkerEmitter WeakMap registry (`f45a052`)

- **agent/history:** Add transcript_marker variant to HistoryEntry (`7e619b8`)

- **agent/events:** Define TranscriptMarker discriminated union (`66860fe`)

- **agent:** Construct TranscriptMarkerEmitter in createDesignSession + history sink (`746b5da`)

- **agent/verbose-transcript:** Subscribe directly to TranscriptMarkerEmitter (§4.7) (`1d86d8a`)

- **agent/events:** Add onTranscriptMarker to subscribeToSession (`3335905`)

- **agent/rpc:** Forward transcript_marker events (§4.7) (`e6d5f2c`)

- **plugin/vc:** Scaffold klayoutclaw_vc submodule (`174d98b`)

- **plugin/vc:** Deterministic GDSII serialiser (DM-1/DM-2/T11) (`8bcfcc0`)

- **plugin/vc:** DM-3 pya code generation (`ee87b10`)

- **plugin/vc:** RepoHandle + atomic git wrapper (RB-1..RB-4/T33/T34) (`55d6e9e`)

- **plugin/vc:** DM-4 memory→disk migration on first save (`1510ca3`)

- **plugin/vc:** DM-5 crash recovery journal (T15) (`9cc8473`)

- **agent/tools:** Add thinking tool (TH-1/TH-2/TH-3) (`9a4c3ac`)

- **agent/tools:** Register thinking in assembleTools + allowlist (TH-4) (`cc10321`)

- **agent/tools/annotations:** Mark thinking readonly (TH-7) (`4e86436`)

- **agent/prompts:** Add thinking guidance (TH-5/T44, resolves OQ-1) (`5a0de40`)

- **agent/tui:** Thinking source prop + App.tsx wiring (TH-6/TH-9/T38) (`3e24ee4`)

- **plugin/vc:** Phase 5 MCP surface — 9 vc_* tool handlers + DM-4 save hook (`e4891b9`)

- **install:** Copy vc_mcp_handlers + klayoutclaw_vc for Phase 5 plugin (`c10e4de`)

- **plugin/vc:** UI-1 status chip (T25/Task 6.1) (`be99bfb`)

- **plugin/vc:** UI-2 checkpoint dialog (T26/Task 6.2) (`bc25ee8`)

- **plugin/vc:** UI-3 history dock panel (T26/Task 6.3) (`9ad5eb4`)

- **plugin/vc:** UI-4 save auto-checkpoint (T27/Task 6.4) (`2a0dc57`)

- **agent/planning:** Add PlanSlugCache (PM-12) (`616b15b`)

- **agent/planning:** Add slugCacheState flag (PM-11 terminal reset) (`9d78d0b`)

- **agent/planning:** Add generateWordSlug + MAX_SLUG_RETRIES (PM-11) (`1f7b926`)

- **plugin/vc:** UI-5 context menus (T32/Task 6.5) (`90aa445`)

- **agent/planning:** Abandon path deletes slug-cache + emits terminal marker (PM-12) (`23fc981`)

- **agent/planning:** Introduce PlanStateMachine + exit_plan_mode marker emission (PM-1, PM-5) (`f327af1`)

- **agent/planning:** PM-8 hard freeze in plan_drafted (T36) (`e3e5c80`)

- **agent/planning:** WaitForPlanApproval pause/resume mechanism (§4.4) (`9661e2f`)

- **agent/planning:** Headless auto-approve + autoApprovePlans coercion (PM-4/T35) (`438d0a9`)

- **agent/planning:** PM-10 permission context swap (T23) (`7923f32`)

- **agent/planning:** Terminal marker + slug-cache lifecycle on approve/abandon/done (PM-7/PM-11) (`b56c46f`)

- **agent/planning:** PM-5 planHash integrity chain (T6) (`ced34c0`)

- **agent/planning:** PM-6 replan loop + blocker classifier (T5/T42) (`a355b21`)

- **agent/planning:** Illegal-transition guard + PlanProtocolError (T41) (`4007df6`)

- **agent/prompts:** Cross-track checkpoint + recovery discipline (§6) (`3ef25c4`)

- **agent/planning:** Periodic plan re-injection after exit (issue #24) (`50580e7`)

- #34 route_inspect labeled-crossings image_path (`cf85476`)

- **detect:** Top_hbn.py — material evidence validation (footprint stays as geometry) (`159a7f1`)

- **detect:** Phase 8 held-out panel runner (held_out_panel.py) (`4b18a1b`)

- **detect:** Graphene.py — footprint-containment scoring (Phase 10a) (`a52893f`)

- **detect:** Graphene.py — footprint-bounded region grow (Phase 10b) (`7cf0c0d`)

- **detect:** Graphene.py — pool-relative contrast filter + absolute-overlap containment (Phase 10c) (`7ab7631`)

- **detect:** Graphene.py — no-grow when seed area is plausible (Phase 10d) (`998b26a`)

- **detect:** Phase 11 composite scoring |relL|^0.25×log(area_um2+1)/30 in graphene.py (`b9bd4ee`)

- **detect:** Graphite.py — tighter contour for tier-1.0 accuracy (Phase 12) (`04af690`)

- **detect:** Graphene.py — footprint-bounded grow + flood_fill (Phase 13) (`956e4d0`)

- **detect:** Graphene.py — polarity-consistent intra-flake bridging (Phase 14) (`6b98d61`)

- **detect:** Graphene.py — auto-discovered footprint informs ranking (Phase 15) (`2e3e9a3`)

- **detect:** Graphite.py — robust substrate/bulk selection (Phase 16) (`1563352`)

- **detect:** Graphite.py — min-chroma-reference strategy for robust achromatic scoring (Phase 19) (`b30c85a`)

- **evaluate_design:** Add route_material_compat self-check primitive (`4a9d025`)

- **auto_route:** Rescue_unrouted_nets — connect the last lead in a dense fan-out (`68a4243`)

- **routing+evaluate:** Qb-opus48 feedback fixes + adaptive two-level auto_route (`d0d9419`)

- **skills:** Add optional SAM2 flake detection wrapper (`1a33202`)

- **sam:** Add MPS inference support (`f9a8947`)

- Package KlayoutClaw for uv installation (`b6e01a9`)

- Configure MCP transport from user settings (`c7be05b`)


### Maintenance

- Remove old rasterize/cost/damping functions and dead variables (`0fe74c5`)

- Add .klayout_roter to gitignore (`29b2878`)

- Delete nanodevice_hallbar skill (`65ee66f`)

- **assets:** Convert logo from PNG to WebP and update README (`2d92905`)

- **simplify:** V0.4.4 post-release cleanup (`531a701`)

- Track .dockerignore for Docker build context (`9bd7dd9`)

- Gitignore Submission/ (`fcc0d36`)

- Configure local agent files (`a0e7607`)

- Validate uv tool artifacts (`7f17667`)

- Distinguish fork plugin identity (`c51e574`)

- Bump fork plugin development version (`ac299dd`)

- Bump fork plugin development version (`b256bf1`)

- Add gated semantic release pipeline (`fd13041`)

- Retain security scans on fork repositories (`75f3e53`)


### Other

- Initial commit (`04421d6`)

- Add KlayoutClaw MCP plugin, UI, docs, and tests

Initial project files for KlayoutClaw: adds the MCP server and UI KLayout macros (plugin/*.lym), installer (install.py), MCP client config (mcp_config.json), tools (tools/gds_to_image.py), tests (tests/*), extensive docs (docs/*), README, CLAUDE.md, TODO, and MIT LICENSE. Also includes .gitignore and Claude settings. Enables running a JSON-RPC MCP server inside KLayout (HTTP on 127.0.0.1:8765) and provides UI status/history, tooling reference, and test scripts for end-to-end verification. (`f16fe52`)

- Add demo GIF capture script and autorouter design docs

- tools/capture_demo.py: step-by-step KLayout screenshot capture using
  QWidget.grab() for full window (with layer panel), combines into GIF
- docs/plans/: autorouter design and implementation plan documents
- .gitignore: exclude generated docs/demo.gif

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com> (`d68102f`)

- Update demo capture with granular step-by-step frames

7 frames: new layout, cell created, layers created, mesa drawn,
bonding pads, pin markers, auto-routed. Full window screenshots
via QWidget.grab() show layer panel with readable names.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com> (`c68fa2e`)

- Improve error handling and add tool busy guard

Add clearer error handling and a single-threaded guard for MCP tool calls. Changes: add .mcp.json MCP server config; update TODO with v0.5.1 tasks; import traceback and format execute_script exceptions to surface user-code frames; improve auto_route errors (parameter hints, install hint for missing route_worker.py, subprocess timeout message, stderr extraction, and missing-output diagnostics); return tool errors as MCP results with isError=true and list available tools when a tool is not found; add _tool_busy/_tool_busy_name to reject parallel tool calls with a retry-friendly error and ensure the busy flag is cleared in finally. These changes make failures more actionable and prevent concurrent execution from corrupting shared layout state. (`e82eef7`)

- Update project description and contact email

Replace the maintainer contact (jiaqi.cai@mit.edu -> caidish1234@gmail.com) in DEVELOPMENT.md and README.md. Revise README intro to clarify MCP client compatibility (mentioning agent harnesses like Claude Code, Codex, Cline or any MCP client), emphasize natural-language layout design and batch edits across GDS files, and simplify the "built for" line to be more concise. (`b669f5c`)

- Add Claude Code skills and screenshot tool

Add a suite of Claude Code skills and image utilities, register the plugin in Claude marketplace, and add a new MCP screenshot tool.

Key changes:
- Add skills/ (geometry, display, image, visual, nanodevice:routing) with CLI scripts and SKILL metadata so Claude can invoke tasks (create geometry, toggle layers, load/list/remove images, routing).
- Add .claude-plugin/plugin.json and .claude-plugin/marketplace.json for Claude Code plugin manifest/catalog.
- Extend plugin/klayoutclaw_server.lym: bump server version to 0.6, register new "screenshot" MCP tool, implement _tool_screenshot, and expose it in dispatch and server info.
- Update docs (CLAUDE.md, README.md, docs/skills.md, docs/tools.md) and TODO.md to document skills, screenshot tool, and autorouter notes.
- Add tests resource image and various helper scripts for skills (mcp_client referenced).

This commit packages skills into the repository, exposes a viewport screenshot MCP tool, and updates docs/manifests to support Claude Code integration and the v0.6 MCP server. (`6d8fa97`)

- Symlink .claude/skills to skills/ for auto-discovery

Enables Claude Code to auto-discover project skills without
plugin marketplace setup. Uses relative symlink so it works
for all users who clone the repo.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com> (`dbe9e28`)

- Preserve raw HTTP body bytes & add UTF-8 tests

Fix body-reading in klayoutclaw_server: stop per-chunk decode/encode that could replace partial UTF-8 sequences and corrupt the payload; instead accumulate raw bytes and decode once. Add a comprehensive test (tests/test_utf8_body_corruption.py) that reproduces and guards against UTF-8 corruption across chunk boundaries (unit + integration modes). Also add "authorization": "none" to .mcp.json and mcp_config.json for explicit configuration. (`bbff917`)

- Merge pull request #2 from caidish/feat/nanodevice-flakedetect

feat: add nanodevice skills (flakedetect + gdsalign) with test suites (`098f303`)

- Update README.md (`680d8c0`)

- Rename DEVELOPMENT.md to CONTRIBUTING.md

Rename DEVELOPMENT.md to CONTRIBUTING.md and update the README link to reference CONTRIBUTING.md. Keeps repository documentation consistent and ensures the contributing link points to the renamed file. (`62b3dc2`)

- Merge branch 'main' of https://github.com/caidish/KlayoutClaw (`14cf609`)

- Update README.md (`0a7615f`)

- Update README.md (`531e285`)

- Merge branch 'main' of https://github.com/caidish/KlayoutClaw (`bc3efd4`)

- Update README (`6c994d5`)

- Bugs Fixed. Picture commitment flip, unstable output dir. (`d1d73e1`)

- Robustness fix. (`7165ffc`)

- Test Fix (`f9dfe2b`)

- Boost refine.py 100x faster (`29d10fd`)

- Eval better with contact isolation. (`32c0f90`)

- Qlaybot Compatible for MCP detect (`d58921e`)

- Plugin + qlaybot + skills fix batch from benchmark review (`003fbaa`)

- MCP CLient fix (`d3cd9e5`)

- 2026-04-14/15 benchmark review baseline (pre-fix) (`61eccb6`)

- Merge branch 'worktree-fix-benchmark-review-2026-04-17' into Qlaybot_Dev

2026-04-14/15 benchmark review fixes:
- De-overfit bulk_containment, route_inspect, _build_next_step, schema
  examples, docs + SKILL.md from Hall-bar-specific defaults.
- New primitive material_overlap_report (kills the most-duplicated
  pattern across all 15 benchmark transcripts).
- New auto_route parameter pin_pairs_override (fixes ml14 Hungarian-
  override blocker that cost 23 sequential auto_route calls).
- Verified crossing_pairs contract (no code fix needed, regression
  guard added).
- Investigated execute_script IndexError under heavy state (did not
  reproduce, reproducer + regression E2E kept as guard).
- 28 new unit tests, 6 new E2E scripts (tmux-free harness, macOS
  portable), all green on live KLayout + MCP.

Plan: docs/superpowers/plans/2026-04-17-benchmark-review-fixes.md
Report: docs/2026-04-17-benchmark-review-update.md

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> (`71adedb`)

- Bug Fix (`e0e6708`)

- Bug Fix (`73ea771`)

- Update Spec for Plan Mode Execution, Thinking Tool, and Klayout Version Control (`8855334`)

- Merge branch 'fix/issue-23-delegate-failure' (fixes #23)

Delegate tool crash fixed + API redesigned (Claude Code AgentTool pattern)
with general-purpose fallback. Plan-mode freeze carve-out + TUI placeholder
cleanup + async race fix for cancel events.

Five rounds of code review with codex (gpt-5 + gpt-5.5 xhigh); final
verdict CLEAN.

Closes #23 (`efbb65a`)

- Merge branch 'feat/issue-24-plan-reinjection' (closes #24)

Plan re-injection after plan mode exit, modeled on Claude Code's
verify_plan_reminder. Periodic plan content re-injection every N user
turns, per-user-turn latch, sentinel-based pruner dedup, /plan verify
to stop reminders, lastTurnWasFailure rollback.

Five rounds of code review with codex (gpt-5 + gpt-5.5 xhigh); final
verdict 1 P2 edge case in promptWithRecovery latch interaction,
tracked as follow-up (not merge-blocking).

Closes #24 (`f347362`)

- Merge branch 'fix/issue-22-thinking-only-termination' (closes #22)

Thinking-only / early-exit termination detector + retry loop with full
non-retryable-error surfacing. Covers every canonical pi-ai failure
shape (thinking-only stops, retryable transport errors, aborted,
stopReason='error' with errorMessage) and handles compacting sessions
correctly via object-identity sinceIdx tracking.

Eight rounds of code review with codex (gpt-5 + gpt-5.5 xhigh) plus
four follow-up fixes on the R8 landing (compaction-length rebind →
identity tracking, context-overflow ordering in lastTurnTerminalError,
HTTP-status-code word-boundaries). Final verdict CLEAN.

Closes #22

# Conflicts:
#	agent/src/cli.ts
#	agent/src/rpc.ts
#	agent/vitest.files.ts (`25989de`)

- Update README.md (`a7d57c0`)

- Merge remote-tracking branch 'origin/main' — bring in README.md update (`0675264`)

- Merge fix/issue-27-cand-D1 — partial fix for #27 (graphite/graphene detection)

Sub-Orch A's best from overnight hill-climb (2026-05-06).
- 29/40 cells passing on 10-stack hill-climb GT (vs 16/36 baseline)
- 2 stacks all-pass (ml04, ml08); 7 stacks have unfixable cells under tried algorithms
- Best-per-material consolidation: graphite from C3 ensemble, graphene + bottom_hBN from C1
- Material counts: graphite 7/10 (was 0/10), graphene 5/10 (was 2/10), bottom_hBN 7/10 (was 5/9), top_hBN 10/10 (parity)

GitHub issue: #27 (still open — gate not met). See:
- STALL.md at .claude/worktrees/subforge-27/STALL.md
- Master under-exploration follow-up at issue #27

Co-Authored-By: Sub-Orch A (overnight hill-climb) (`51d1958`)

- GrabCut + black-border padding + quality-gate retry (`1f01564`)

- Merge fix/issue-32-cand-B1 — fix for #32 (footprint GrabCut degeneracy)

Sub-Orch B's best from overnight hill-climb (2026-05-06).
- GrabCut + black-border padding (≥50px or max(H,W)//30) prevents whole-image quadrilateral
- Inline structural quality gates: n_points >= 8, area/image_area < 0.85
- 2x more aggressive seed erosion + retry up to 3 attempts
- Emits status: "failed" non-zero on final degeneracy
- combine/scripts/transform.py refuses footprints with status in {"needs_rotation_selection", "failed"}

Verified byte-identical to main on stacks where main's GrabCut works on attempt 1
(AH02 spot-check, all 4 materials). Pure improvement, no regression.

GitHub issue: #32 (still open — gate at 15/40 not met because of unrelated #27 graphite defect).
See STALL.md at .claude/worktrees/subforge-32/STALL.md.

Co-Authored-By: Sub-Orch B (overnight hill-climb) (`3dfdb89`)

- Merge fix/issue-28-cand-C3 — fix for #28 (route_worker bus + ordered-loop)

Sub-Orch C's best from overnight hill-climb (2026-05-06).
- Hungarian assignment replaced by ordered-loop cyclic-monotonic DP (eliminates inter-net crossings at assignment stage)
- Per-individual-polygon pin clearance (instead of merged-region interacting()) — fixes "this pin only" intent on Hall-bar designs where contacts straddle mesa edge
- Global obstacle inflation by path_width//2 — enforces centerline >= path_width/2 from raw obstacles, eliminates path-rasterization gap
- Steiner branch (find_path_to_existing) for shared-pad multi-pin nets via bus_pairs schema
- 3/3 regression tests pass: test_3pin_ybus, test_singleton_via_bus_pairs, test_bus_pairs_omitted_falls_back_to_ordered_loop

All 5 fixtures (AH06, HM05, HM06, HM07, QH10) achieve iso=1.0, forbidden=0, ep=1.0, route×route=0.
Connectivity drops in tight (<2µm) contact corridors — known limitation, documented in STALL.md.

Backward-compatible: bus_pairs and freeze_completed_routes_as_obstacles_with_margin are optional.

GitHub issue: #28 (still open — gate not met due to connectivity drop in tight clusters).
See STALL.md at .claude/worktrees/subforge-28/STALL.md.

Co-Authored-By: Sub-Orch C (overnight hill-climb) (`82e14e0`)

- Merge pull request #41 from caidish/fix/issue-35-doc-execute-script

docs: #35 execute_script import availability (`73a998b`)

- Merge pull request #42 from caidish/fix/issue-37-doc-restart

docs: #37 KLayout restart recovery procedure (`09e3ffc`)

- Merge pull request #43 from caidish/fix/issue-31-footprint-warp

fix: #31 footprint.py --warp PATH (reuse precomputed SIFT) (`c61a1ee`)

- Merge pull request #44 from caidish/fix/issue-33-combine-diagnostics

fix: #33 per-stage diagnostics in combine.transform (`4fb8bff`)

- Merge pull request #45 from caidish/fix/issues-25-34-server-improvements

fix: #25 + #34 server tool list cleanup + route_inspect crossings image (`2b8ac13`)

- Merge pull request #46 from caidish/fix/issue-36-planner-prefix

fix: #36 PLANNER, NOT EXECUTOR prefix on planner tool descriptions (`72028ef`)

- Bump pi-ai/pi-coding-agent/pi-tui to 0.70.0 and migrate breaking APIs (`0416f52`)

- Render whole design + follow active tab (`001d008`)

- Pre/post snapshot + damage recovery (`9489cbd`)

- Principle-driven graphite + three-candidate architecture (`19b8e56`)

- Bundle ordered_loop.py with route_worker; gitignore agent dist (`9771598`)

- Suppress IDE noise, paper draft, and local config (`c80b79e`)

- Configurable bind via KLAYOUT_MCP_BIND env var (`91b1251`)

- Auto_route reads PYTHON_PATH env var before conda fallback (`29f3103`)

- Klayoutclaw-side artifacts from docker sidecar work (`5ce69d1`)

- Replace graphite + bottom_hbn detectors with adaptive pipeline (`2d3cbb4`)

- Update flakedetect bottom hBN dilation and graphene candidates (`b72123f`)

- Merge pull request #47 from caidish/fix-bottom_hbn

Update flakedetect bottom hBN dilation and graphene candidates (`ca8fc99`)

- Align SAM flakedetect skill workflow (`83220ed`)

- Integrate fix-bottom_hbn updates (`7d56e56`)

- Update nanodevice flake detect skills (`b36cfba`)

- Update flake detection skills (`ef5b2ab`)

- Clarify default SAM flake detection workflow (`d798885`)

- Tighten flake detect SAM workflow (`f1ecba6`)

- Tighten graphene SAM flood controls (`4754dc7`)

- Preserve multi-component graphite in combine (`45bf786`)

- Merge configurable MCP port support (`cbefabe`)

- Merge uv-compatible installation support (`acd3e75`)

- Merge Claude Desktop MCP launcher compatibility (`e26e6a1`)

- Merge pull request #1 from aRustyDev/integration/fork-main-dev2

fix: make marketplace MCP launcher Desktop-compatible (`82d4f69`)

- Merge inline Claude Desktop MCP launcher (`53a1c70`)

- Merge pull request #2 from aRustyDev/integration/fork-main-dev3

fix: remove Desktop MCP placeholder dependency (`3614ff3`)

- Merge configurable MCP transport settings

# Conflicts:
#	install.py (`d3e982e`)

- Merge pull request #3 from aRustyDev/integration/fork-main-dev4

feat: integrate configurable MCP transport settings (`a77287c`)

- Merge uv packaging prerequisite

# Conflicts:
#	install.py (`10a8d82`)

- Merge release automation for initial PyPI publication (`172ae3b`)

- Merge pull request #4 from aRustyDev/integration/fork-main-release

ci: enable initial PyPI release automation (`74d2df7`)

- Merge pull request #5 from aRustyDev/fix/release-test-dependencies

fix: install release test dependencies (`40df605`)


### Refactoring

- Replace matplotlib rasterization with kdb.Region.rasterize() (`a81030d`)

- Rewrite evaluate_worker.py with configurable check primitives (`7a2562c`)

- Make --bottom required in footprint.py, remove color-mode fallback (`5c5d1d6`)

- **agent/planning:** Replace plan-<ts> with word-slug + PlanSlugCache (PM-11) (`492d3c5`)

- **agent/tui:** Rename PlanExitMenu → PlanApprovalMenu + rewire actions (PM-3/T31) (`7904cf5`)

- **agent:** Prune review-cycle comments from thinking-only guard flow (`475174c`)

- **detect:** Graphite.py — adaptive substrate, host, scoring (no GT priors) (`83782e4`)

- **detect:** Graphite.py — address Phase 1 spec deviations (`7d01732`)

- **detect:** Graphite.py — restore physics-grounded weights (universal, not GT-fit) (`7916849`)

- **detect:** Graphite.py — address Phase 1 caveats (chroma cap, s_central, docstring) (`2120a59`)

- **detect:** Graphene.py — remove GT priors, PDMS branch, center placeholder (`d040963`)

- **detect:** Bottom_hbn.py — classify hBN instead of inheriting host (+ Phase 1 carryovers) (`d737b81`)

- **detect:** B1_classifier — per-image logistic + Otsu + physical kernels (no stored coefs) (`d0b6aae`)

- **detect:** B2_multik — silhouette K, chi2 Mahalanobis, no GT priors (`d058430`)

- **detect:** B3_shapetemplate — per-image weights, multiotsu contrast polarity, no GT priors (`e0ff7af`)


### Reverts

- **readme:** Remove incorrect user-attachments URL from E2E demo embed (`23f197e`)


### Testing

- Add unrouted Hall bar GDS creator with pin markers (`aa25860`)

- Add routing structural validator (`02a4485`)

- Add E2E autoroute test script (`b0b9b81`)

- Enlarge bonding pads to 300x300um for harder routing (`9aa0a6b`)

- Add conftest + flakedetect core/align tests (10 passing) (`cadfc15`)

- Add nanodevice test suites with ML08 fixtures (41 tests) (`51babe6`)

- Qlaybot v0.4.1 — 697 agent tests + 8 functional MCP test suites (`bf5820c`)

- Rewrite evaluate_worker tests for configurable check primitives (`88d807f`)

- **evaluate:** Strengthen bulk_containment error-path assertion (`f02c9f5`)

- **schema:** Make layer_map Hall-bar detector load-bearing (`54a7648`)

- **e2e:** Non-Hall-bar evaluate_design full pipeline (`0a4f6a5`)

- **evaluate:** Failing tests for material_overlap_report primitive (`e7a35c6`)

- **e2e:** Material_overlap_report end-to-end (`630af2f`)

- **route:** Failing tests for pin_pairs_override parameter (`1fefbae`)

- **e2e:** Pin_pairs_override end-to-end (`004f44e`)

- **evaluate:** Regression guard — crossing_pairs populates on real crossings (`6b77fff`)

- **e2e:** Crossing_pairs populated end-to-end (`17f24df`)

- **server:** Reproducer + regression for execute_script heavy state (`bb28f1d`)

- **e2e:** Heavy-state execute_script regression (`a173d9d`)

- **e2e:** Alt-device full pipeline proves de-overfit + new primitives stack (`af809bd`)

- **e2e:** Regression bundle runs every phase E2E sequentially (`ba240e5`)

- **plugin/vc:** Add VC plugin test suite for Phase 4 (51 tests) (`423ae0d`)

- **agent/tools:** Add T29 thinking schema probe (`ef879c3`)

- **agent/compaction:** T30 thinking-marker isolation (TH-13) (`c624901`)

- **agent/e2e:** Task 1.8 integration suite green (T1/T7/T19/T20/T21/TH-10) (`a701a49`)

- **plugin/vc:** Phase 5 MCP handler unit tests (41 tests) (`2f6f9b4`)

- **plugin/vc:** Phase 5 plugin-side tools/list regression (3 live tests) (`642a247`)

- **agent/mcp:** Assert 9 klayout_native_vc_* tools wired (Task 5.10) (`969ff57`)

- **agent:** Phase 1 thinking-tool test suite (Tasks 1.1-1.8 / TH-1..TH-14) (`5ca7124`)

- **agent/planning:** T37 planLengthChars coverage (PM-13) (`20c780c`)

- **agent/tools/delegate:** T22 subagent blocked during plan mode (PM-9) (`5e14e34`)

- **agent:** Rebase v0.4.3 plan-mode tests for v0.4.4 refactor (T8) (`35117bc`)

- **agent/e2e:** Phase 2b integration suite (T2/T3/T4/T24/T39/T43) (`a120485`)

- **agent/e2e:** T17 + T18 cross-track soft assertions (`16ac52e`)

- **agent:** T16 graceful-degradation (spec §9.2 Track 2) (`17c777c`)

- **agent/e2e:** Harden T24 + T19(b) prompts against real-API variance (G4 flag) (`26d269a`)

- **agent:** T19(b) native-surface soft-demote + thinkingLevel fix (`73d0170`)

- **agent/e2e:** Retry harness + soft fallthrough for model-variance paths (`b131af2`)

- IoU verifier for graphite & bottom_hBN against bench GT (`ba2eb09`)

- **detect:** Freeze detector mask baselines on mlxx for regression gate (`e90b133`)

- **detect:** IoU regression + generality property tests (initially red) (`2397a4a`)

- **detect:** Address Phase 0 code-review feedback (`f1fd2c9`)

- **detect:** Replace snapshot gate with GT-evaluator regression (`0491e16`)

- **detect:** Add agent-driven detector regression gate (replaces static IoU baseline) (`f000093`)

- **detect:** Extend regression to 18 stacks at 0.8 floor (initially red) (`5f99d0c`)

- Remove stale graphene grow assertion (`e43eb8f`)

- Cover configurable MCP endpoint contract (`bfbf032`)

- Align single-server config fallback (`9a9c1d4`)

