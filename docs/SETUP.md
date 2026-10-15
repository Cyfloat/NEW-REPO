# Team setup and first walkthrough

## 1. One-time setup (each person)
1. Install Git, Python 3.10+, and Claude Code. On Windows, Git for Windows (Git Bash) is needed.
2. Make sure `python` runs from your terminal — the hook calls `python`.
   (If only `python3` works on your machine, tell the repo owner; don't edit the shared settings.)
3. Sign in to Claude Code with your company-approved account.
4. Clone the repo, `pip install -e ".[dev]"`, run `pytest -q`.
5. Run `claude` in the repo root and accept the trust prompt.
6. Personal preferences go in `.claude/settings.local.json` (gitignored), never in `settings.json`.

## 2. Check your setup works
In a Claude session on `main`, ask: *"Add a comment to the top of CLAUDE.md."*
Expected: the hook **denies** it (no ticket in branch name). If the edit goes through, your
hook isn't running — check `python` is on PATH and you accepted the trust prompt.

## 3. First walkthrough: TOY-1
1. `git checkout -b feat/TOY-1-pick-rate-metric`
2. Start Claude in plan mode: `claude --permission-mode plan`
3. Prompt: *"Read intent/TOY-1-pick-rate-metric/intent.md. Write spec.md next to it, resolving
   the open question with a recommendation. Then interview me on anything ambiguous and
   propose a plan. When I approve, write it to plan.md."*
4. Review and commit spec.md and plan.md.
5. Leave plan mode (Shift+Tab) and ask Claude to implement plan.md, run tests and lint, and fix failures.
6. Ask: *"Use the verifier subagent to check this work."* Fix anything it fails.
7. Push the branch and open a PR using the template. A human reviews and merges.

## 4. Starting new work
`/new-intent TOY-2 some-slug "one-line idea"` — then repeat the walkthrough.

## Who changes what
| File | Who | How |
|---|---|---|
| `CLAUDE.md` | Anyone | PR, reviewed by CODEOWNER |
| `.claude/*` | Anyone | Ticket branch + human approval in-session + CODEOWNER review |
| `intent/*` | Originator writes, reviewer accepts | PR |
