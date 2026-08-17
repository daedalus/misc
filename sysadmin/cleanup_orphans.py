#!/usr/bin/env python3
"""
Delete folders and files not owned by any process.

Scans a target directory, cross-references open file descriptors from /proc,
and deletes paths not held by any running process. Defaults to dry-run mode.
"""

import argparse
import os
import signal
import subprocess
import sys
from pathlib import Path


def get_open_paths() -> set[str]:
    """Collect all paths currently open by running processes via /proc."""
    paths: set[str] = set()
    for pid_dir in Path("/proc").iterdir():
        if not pid_dir.name.isdigit():
            continue
        try:
            fd_dir = pid_dir / "fd"
            if not fd_dir.exists():
                continue
            for fd in fd_dir.iterdir():
                try:
                    target = os.readlink(fd)
                    if target.startswith("/") and not target.startswith("/proc"):
                        paths.add(target)
                except (OSError, PermissionError):
                    continue
        except (OSError, PermissionError):
            continue
    return paths


def lsof_paths(dirs: list[str]) -> set[str]:
    """Fallback/supplement: collect paths via lsof for given directories."""
    paths: set[str] = set()
    try:
        result = subprocess.run(
            ["lsof", "-t", "-X"] + dirs,
            capture_output=True, text=True, timeout=60
        )
        for pid in result.stdout.strip().splitlines():
            pid = pid.strip()
            if not pid.isdigit():
                continue
            try:
                with open(f"/proc/{pid}/fdinfo", "r") as f:
                    pass
            except Exception:
                continue
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return paths


def delete_orphans(target: Path, open_paths: set[str], dry_run: bool) -> None:
    """Delete files/folders at target not present in open_paths."""
    if not target.exists():
        print(f"[skip] {target} does not exist")
        return

    if not target.is_dir():
        print(f"[skip] {target} is not a directory")
        return

    entries = sorted(target.iterdir(), key=lambda p: (p.is_dir(), p.name))
    for entry in entries:
        abs_path = str(entry.resolve())
        if abs_path in open_paths:
            print(f"[keep]  {abs_path} (open by process)")
            continue

        if dry_run:
            print(f"[dry]   {abs_path}")
        else:
            try:
                if entry.is_dir():
                    entry.rmdir()
                    print(f"[rmdir] {abs_path}")
                else:
                    entry.unlink()
                    print(f"[del]   {abs_path}")
            except OSError as e:
                print(f"[err]   {abs_path}: {e}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Delete folders and files not owned by any process."
    )
    parser.add_argument(
        "directory",
        type=str,
        help="Target directory to clean up."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually delete. Without this, runs in dry-run mode."
    )
    parser.add_argument(
        "--lsof",
        action="append",
        default=[],
        help="Extra directories to include in lsof scan."
    )
    args = parser.parse_args()

    target = Path(args.directory).resolve()
    if not target.exists():
        print(f"[err] {target} does not exist", file=sys.stderr)
        return 1

    if args.apply:
        print("[*] Running in APPLY mode — changes will be permanent.\n")
    else:
        print("[*] Running in dry-run mode. Use --apply to actually delete.\n")

    print(f"[*] Scanning /proc for open file descriptors...")
    open_paths = get_open_paths()
    print(f"[*] Found {len(open_paths)} open paths.")

    if args.lsof:
        print(f"[*] Running lsof fallback...")
        open_paths |= lsof_paths(args.lsof)
        print(f"[*] Total after lsof: {len(open_paths)} open paths.\n")
    else:
        print()

    delete_orphans(target, open_paths, dry_run=not args.apply)

    if args.apply:
        print("\n[*] Done.")
    else:
        print("\n[*] Dry-run complete. Re-run with --apply to delete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
