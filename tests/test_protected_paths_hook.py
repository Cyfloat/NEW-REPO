"""Tests for the governance hook. Test the DENY path, not just the happy path."""

import json
import subprocess
import sys
from pathlib import Path

from protected_paths import decide

ROOT = "/repo"
HOOK = Path(__file__).resolve().parents[1] / ".claude" / "hooks" / "protected_paths.py"


def payload(path):
    return {"tool_name": "Edit", "tool_input": {"file_path": path}}


def decision(result):
    return result["hookSpecificOutput"]["permissionDecision"] if result else None


def test_normal_code_has_no_opinion():
    assert decide(payload("/repo/src/toyapp/metrics.py"), "main", ROOT) is None


def test_governance_file_without_ticket_is_denied():
    assert decision(decide(payload("/repo/.claude/settings.json"), "feat/cleanup", ROOT)) == "deny"
    assert decision(decide(payload("/repo/CLAUDE.md"), "main", ROOT)) == "deny"


def test_governance_file_with_ticket_asks_human():
    result = decide(payload("/repo/.github/CODEOWNERS"), "feat/TOY-7-owners", ROOT)
    assert decision(result) == "ask"


def test_windows_paths_are_handled():
    result = decide(payload("C:\\work\\repo\\.claude\\hooks\\x.py"), "main", "C:\\work\\repo")
    assert decision(result) == "deny"


def test_malformed_input_fails_closed():
    proc = subprocess.run(
        [sys.executable, str(HOOK)], input="not json", capture_output=True, text=True
    )
    assert proc.returncode == 0
    assert decision(json.loads(proc.stdout)) == "deny"
