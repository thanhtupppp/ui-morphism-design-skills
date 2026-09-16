#!/usr/bin/env python3
"""CLI compatibility wrapper for the Skill package validator."""
from skill_validator import *  # noqa: F401,F403
from skill_validator import run_cli


if __name__ == "__main__":
    raise SystemExit(run_cli())
