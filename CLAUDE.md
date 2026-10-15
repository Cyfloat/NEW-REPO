# CLAUDE.md — project guide for Claude Code

This file loads at the start of every Claude Code session. The whole team maintains it.
When Claude makes a mistake worth not repeating, add a line under "Known mistakes" in a PR.

## What this repo is
A toy Python project used to prove an AI-native SDLC workflow before moving it to the
enterprise Bitbucket repo. Contains no client code or data, and must never contain any.

## Commands (the feedback loop — run these before reporting any task done)
- Install: `pip install -e ".[dev]"`
- Test: `pytest -q`
- Lint: `ruff check .`
- Format check: `ruff format --check .`

## Layout
- `src/toyapp/` — package code
- `tests/` — pytest tests, one file per module
- `intent/<TICKET-ID>-<slug>/` — work items: intent.md -> spec.md -> plan.md
- `.claude/` — shared agent config (hooks, agents, skills, commands). Changes need CODEOWNER review.

## Artifact chain (read before changing anything)
- Every task belongs to a work item in `intent/<TICKET-ID>-<slug>/`.
- Before editing code, read that work item's `plan.md`. If none exists, stop and ask for one.
  Do not invent scope.
- If you must deviate from `plan.md`, record the deviation and reason under
  `## Deviations` in plan.md before continuing.
- Branch names carry the ticket ID: `feat/TOY-1-short-description`.

## Protected paths
- `.claude/`, `CLAUDE.md`, and `.github/` are governance files. A hook blocks edits unless the
  branch name contains a ticket ID, and then asks a human to approve. Don't route around it.

## Known mistakes
- (add entries here as they happen)
