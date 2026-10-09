#!/usr/bin/env python3
"""
Update script for managing Ansible roles in _data/ansible_roles.yml

Usage:
    python scripts/update_roles.py add <role_name> [<role_name> ...]
    python scripts/update_roles.py remove <role_name> [<role_name> ...]
    python scripts/update_roles.py list
    python scripts/update_roles.py sync
    python scripts/update_roles.py regenerate

The role list is stored in _data/ansible_roles.yml and is used by index.md
to auto-generate the Ansible roles table.
"""

import sys
import os
import json
import urllib.error
import urllib.request
import yaml

ROLES_FILE = "_data/ansible_roles.yml"
ROLE_REPOSITORIES_FILE = "_data/ansible_role_repositories.yml"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GITHUB_OWNER = "buluma"
ROLE_REPOSITORY_PREFIX = "ansible-role-"


def load_roles():
    """Load roles from YAML file."""
    filepath = os.path.join(REPO_ROOT, ROLES_FILE)
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)
    # YAML loads as a list directly
    return set(data) if data else set()


def save_roles(roles):
    """Save roles to YAML file, maintaining sorting and formatting."""
    filepath = os.path.join(REPO_ROOT, ROLES_FILE)
    sorted_roles = sorted(roles)

    with open(filepath, "w") as f:
        f.write("# Ansible Roles Index\n")
        f.write("# Auto-generated - DO NOT EDIT MANUALLY\n")
        f.write(
            "# Edit this file or use: python scripts/update_roles.py add|remove <role_name>\n"
        )
        f.write("\n")
        for role in sorted_roles:
            f.write(f"- {role}\n")

    print(f"Updated {len(sorted_roles)} roles in {ROLES_FILE}")


def save_role_repositories(repositories):
    """Save GitHub repository slugs for roles whose Galaxy names differ."""
    filepath = os.path.join(REPO_ROOT, ROLE_REPOSITORIES_FILE)
    with open(filepath, "w") as f:
        yaml.safe_dump(repositories, f, sort_keys=True)


def cmd_add(role_names):
    """Add one or more roles."""
    roles = load_roles()
    added = []
    for name in role_names:
        if name in roles:
            print(f"Role '{name}' already exists, skipping")
        else:
            roles.add(name)
            added.append(name)

    if added:
        save_roles(roles)
        print(f"Added: {', '.join(added)}")
    else:
        print("No new roles added")


def cmd_remove(role_names):
    """Remove one or more roles."""
    roles = load_roles()
    removed = []
    for name in role_names:
        if name in roles:
            roles.remove(name)
            removed.append(name)
        else:
            print(f"Role '{name}' not found, skipping")

    if removed:
        save_roles(roles)
        print(f"Removed: {', '.join(removed)}")
    else:
        print("No roles removed")


def cmd_list():
    """List all roles."""
    roles = load_roles()
    print(f"Total roles: {len(roles)}")
    for role in sorted(roles):
        print(f"  - {role}")


def cmd_sync():
    """Synchronize roles from non-archived public GitHub role repositories."""
    roles = set()
    role_repositories = {}
    page = 1
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    while True:
        url = (
            f"https://api.github.com/users/{GITHUB_OWNER}/repos"
            f"?type=public&per_page=100&page={page}"
        )
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        if token:
            request.add_header("Authorization", f"Bearer {token}")

        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                repositories = json.load(response)
        except urllib.error.HTTPError as error:
            raise RuntimeError(
                f"GitHub API request failed with HTTP {error.code} on page {page}"
            ) from error

        if not isinstance(repositories, list):
            raise RuntimeError("GitHub API returned an unexpected repository response")
        if not repositories:
            break

        for repository in repositories:
            name = repository.get("name", "")
            if repository.get("archived") or not name.startswith(ROLE_REPOSITORY_PREFIX):
                continue
            repository_role = name.removeprefix(ROLE_REPOSITORY_PREFIX)
            role_name = repository_role.replace("-", "_")
            roles.add(role_name)
            if role_name != repository_role:
                role_repositories[role_name] = repository_role

        page += 1

    if not roles:
        raise RuntimeError(
            f"No active {ROLE_REPOSITORY_PREFIX} repositories found for {GITHUB_OWNER}; "
            "refusing to replace the current role list"
        )

    save_roles(roles)
    save_role_repositories(role_repositories)
    print(f"Synchronized roles from {GITHUB_OWNER}'s active public repositories")


def cmd_regenerate():
    """
    Regenerate ansible_roles.yml from index.md Liquid template output.
    Parses the {% for role in site.data.ansible_roles %} loop to extract role names.
    """
    import re

    filepath = os.path.join(REPO_ROOT, ROLES_FILE)

    # Try to extract from index.md Liquid template
    index_path = os.path.join(REPO_ROOT, "index.md")
    with open(index_path, "r") as f:
        content = f.read()

    # Match the Liquid template pattern
    pattern = (
        r"\|\\\[\{\{ role \}\}\\]\(https://galaxy\.ansible\.com/buluma/\{\{ role \}\}\)"
    )
    if pattern in content:
        print("Found Liquid template pattern in index.md")
        print("Cannot regenerate from Liquid template - roles must be managed manually")
        return

    # Alternative: try to find hardcoded role links in the file
    roles = sorted(
        set(
            re.findall(
                r"\[([a-zA-Z0-9_-]+)\]\(https://galaxy\.ansible\.com/buluma/", content
            )
        )
    )

    if not roles:
        print("No roles found in index.md")
        return

    # Save the roles
    with open(filepath, "w") as f:
        f.write("# Ansible Roles Index\n")
        f.write("# Auto-generated - DO NOT EDIT MANUALLY\n")
        f.write(
            "# Edit this file or use: python scripts/update_roles.py add|remove <role_name>\n"
        )
        f.write("\n")
        for role in roles:
            f.write(f"- {role}\n")

    print(f"Regenerated {len(roles)} roles in {ROLES_FILE}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing role name(s)")
            print(
                "Usage: python scripts/update_roles.py add <role_name> [<role_name> ...]"
            )
            sys.exit(1)
        cmd_add(sys.argv[2:])

    elif command == "remove":
        if len(sys.argv) < 3:
            print("Error: Missing role name(s)")
            print(
                "Usage: python scripts/update_roles.py remove <role_name> [<role_name> ...]"
            )
            sys.exit(1)
        cmd_remove(sys.argv[2:])

    elif command == "list":
        cmd_list()

    elif command == "sync":
        cmd_sync()

    elif command == "regenerate":
        cmd_regenerate()

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
