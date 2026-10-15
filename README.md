# NEW-REPO — AI-native SDLC sandbox

A toy Python project for rehearsing an AI-native SDLC with Claude Code before moving the
pattern to the enterprise Bitbucket repo. **No client code, data, or names — ever. This repo is public.**

## Quick start
```bash
git clone https://github.com/Cyfloat/NEW-REPO.git
cd NEW-REPO
pip install -e ".[dev]"
pytest -q
claude            # accept the workspace-trust prompt so project hooks/settings load
```
New teammates: read [docs/SETUP.md](docs/SETUP.md) first.

## How work flows
`intent.md` → `spec.md` → `plan.md` → code + tests → verifier → PR → human review → merge.
Each artifact lives in `intent/<TICKET-ID>-<slug>/` and is committed with the code.

## What's in `.claude/`
| Path | Purpose |
|---|---|
| `settings.json` | Shared permissions and hooks (applies to everyone) |
| `hooks/protected_paths.py` | Blocks edits to governance files without a ticket branch; fails closed |
| `agents/verifier.md` | Independent end-of-task check against plan.md |
| `skills/python-standards/` | Team coding standards Claude applies automatically |
| `commands/new-intent.md` | `/new-intent` slash command to start a work item |
