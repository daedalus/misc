#!/usr/bin/env python3
import subprocess
import json
import os
import sys


def get_non_forked_repos(username, max_pages=5):
    repos = []
    for page in range(1, max_pages + 1):
        result = subprocess.run(
            [
                "curl",
                "-s",
                f"https://api.github.com/users/{username}/repos?per_page=100&page={page}",
            ],
            capture_output=True,
            text=True,
        )
        try:
            data = json.loads(result.stdout)
            if not data:
                break
            repos.extend([r["full_name"] for r in data if not r.get("fork", False)])
        except json.JSONDecodeError:
            print(f"Warning: Failed to parse page {page}", file=sys.stderr)
    return sorted(set(repos))


def clone_repos(repos, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    original_dir = os.getcwd()

    try:
        os.chdir(target_dir)
        success = 0
        failed = 0

        for repo in repos:
            print(f"Cloning {repo}...")
            result = subprocess.run(
                ["git", "clone", f"https://github.com/{repo}.git"], capture_output=True
            )
            if result.returncode == 0:
                success += 1
            else:
                failed += 1
                print(f"  Failed: {repo}", file=sys.stderr)

        return success, failed
    finally:
        os.chdir(original_dir)


def main():
    username = "daedalus"
    target_dir = "daedalus-repos"

    print(f"Fetching non-forked repositories for {username}...")
    repos = get_non_forked_repos(username)

    if not repos:
        print("No repositories found!", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(repos)} non-forked repositories")
    print(f"Cloning to {target_dir}...")

    success, failed = clone_repos(repos, target_dir)
    print(f"Done! Cloned {success} repos, {failed} failed.")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
