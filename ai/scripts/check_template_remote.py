#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys


TEMPLATE_OWNER = "Loligplayer33"
TEMPLATE_REPO = "research-vault-template"
TEMPLATE_SLUG = f"{TEMPLATE_OWNER.lower()}/{TEMPLATE_REPO.lower()}"


def run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def normalize_remote(url: str) -> str:
    value = url.strip().lower()
    if value.endswith(".git"):
        value = value[:-4]
    value = value.replace("https://github.com/", "")
    value = value.replace("http://github.com/", "")
    value = value.replace("ssh://git@github.com/", "")
    value = value.replace("git@github.com:", "")
    return value.rstrip("/")


def main() -> int:
    inside = run_git(["rev-parse", "--is-inside-work-tree"])
    if inside.returncode != 0 or inside.stdout.strip() != "true":
        print("No Git repository detected.")
        print()
        print("If this vault was downloaded as a ZIP, create your own repository before project setup:")
        print("  git init")
        print("  git add .")
        print('  git commit -m "Initialize research vault"')
        print("  git remote add origin <your-new-repo-url>")
        print("  git push -u origin main")
        return 1

    origin = run_git(["remote", "get-url", "origin"])
    if origin.returncode != 0:
        print("No Git remote named 'origin' is configured.")
        print()
        print("Create a new repository under your own account, then connect it:")
        print("  git remote add origin <your-new-repo-url>")
        print("  git push -u origin main")
        return 1

    origin_url = origin.stdout.strip()
    normalized = normalize_remote(origin_url)

    if normalized == TEMPLATE_SLUG:
        print("This vault is still connected to the upstream template repository:")
        print(f"  origin -> {origin_url}")
        print()
        print("Do not track your project work in the template repository.")
        print("Use GitHub's 'Use this template' button, or create your own empty repository and run:")
        print("  git remote set-url origin <your-new-repo-url>")
        print("  git push -u origin main")
        print()
        print("If you are the template developer intentionally editing the template, continue in developer/test mode.")
        return 2

    print("Git remote check passed.")
    print(f"origin -> {origin_url}")
    print("This does not point to the upstream template repository.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
