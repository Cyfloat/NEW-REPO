"""PreToolUse gate: governance files need a ticket ID in the branch name + human approval.

Fails CLOSED: any unexpected error produces a "deny" decision, never a silent pass.
Exit code is always 0 with a JSON decision (exit 1 would be a non-blocking error = fail open).
"""

import json
import os
import re
import subprocess
import sys

PROTECTED_PREFIXES = (".claude/", ".github/")
PROTECTED_FILES = ("CLAUDE.md",)
TICKET_RE = re.compile(r"[A-Z][A-Z0-9]+-\d+")


def decide(payload: dict, branch: str, project_dir: str) -> dict | None:
    """Return a hook decision dict, or None for 'no opinion'."""
    file_path = (payload.get("tool_input") or {}).get("file_path") or ""
    if not file_path:
        return None

    norm = file_path.replace("\\", "/")
    root = project_dir.replace("\\", "/").rstrip("/") + "/" if project_dir else ""
    rel = norm[len(root) :] if root and norm.startswith(root) else norm
    if rel.startswith("./"):
        rel = rel[2:]

    protected = rel.startswith(PROTECTED_PREFIXES) or rel in PROTECTED_FILES
    if not protected:
        return None

    ticket = TICKET_RE.search(branch or "")
    if not ticket:
        return _out(
            "deny",
            f"'{rel}' is a governance file. Work on a branch named with a "
            f"ticket ID (e.g. feat/TOY-12-update-hooks), then retry.",
        )
    return _out(
        "ask",
        f"'{rel}' is a governance file (ticket {ticket.group(0)}). A human must approve this edit.",
    )


def _out(decision: str, reason: str) -> dict:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason,
        }
    }


def current_branch(project_dir: str) -> str:
    try:
        return subprocess.run(
            ["git", "-C", project_dir or ".", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
    except Exception:
        return ""


def main() -> None:
    try:
        payload = json.load(sys.stdin)
        project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
        result = decide(payload, current_branch(project_dir), project_dir)
    except Exception as exc:  # fail closed
        result = _out("deny", f"Gate error ({exc.__class__.__name__}); edit blocked for safety.")
    if result:
        print(json.dumps(result))
    sys.exit(0)


if __name__ == "__main__":
    main()
