#!/usr/bin/env python3
"""Create an independent Better Research workspace without copying Git history."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def rewrite_project_brief(destination: Path, project_name: str) -> None:
    brief = destination / "research" / "project-brief.md"
    text = brief.read_text(encoding="utf-8")
    text = text.replace("Workspace mode: TEMPLATE.", "Workspace mode: RESEARCH.")
    text = text.replace(
        "Research project name: NOT YET FILLED.",
        f"Research project name: {project_name}.",
    )
    brief.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create an independent Better Research research repository."
    )
    parser.add_argument("destination", help="New directory to create")
    parser.add_argument(
        "--name",
        help="Research project name; defaults to destination directory name",
    )
    parser.add_argument("--remote", help="Optional Git remote URL")
    parser.add_argument(
        "--no-git",
        action="store_true",
        help="Copy and configure the workspace without initializing Git",
    )
    args = parser.parse_args()

    destination = Path(args.destination).expanduser().resolve()
    if destination.exists():
        print(f"Destination already exists: {destination}", file=sys.stderr)
        return 2

    project_name = args.name or destination.name

    def ignore(directory: str, names: list[str]):
        ignored = {".git", ".DS_Store", "__pycache__"}
        return ignored.intersection(names)

    shutil.copytree(ROOT, destination, ignore=ignore)
    rewrite_project_brief(destination, project_name)

    if args.no_git:
        print(f"Created RESEARCH workspace at {destination}")
        return 0

    try:
        run(["git", "init"], destination)
        run(["git", "add", "."], destination)
        run(
            ["git", "commit", "-m", "chore: initialize research workspace"],
            destination,
        )
        run(["git", "branch", "-M", "main"], destination)
        if args.remote:
            run(["git", "remote", "add", "origin", args.remote], destination)
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(
            "Workspace files were created, but Git initialization did not complete. "
            f"Resolve Git locally and continue in {destination}. Error: {exc}",
            file=sys.stderr,
        )
        return 1

    print(f"Created RESEARCH workspace at {destination}")
    if args.remote:
        print("Remote configured. Review the project brief before the first push.")
    else:
        print("No remote configured. Add one after creating a private repository.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
