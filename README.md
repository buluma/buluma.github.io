---
layout: default
title: buluma.github.io
---

# buluma.github.io

This repository contains the content for the Buluma site, including:

- Pages and posts
- Documentation
- Ansible role index (`index.md`)

## Documentation

Comprehensive documentation for this repository is available in the `docs/`
directory:

- **README.md**: Project overview and structure
- **project-overview.md**: Detailed project goals and roadmap
- **code-standards.md**: Coding standards for Markdown, HTML, CSS, and
  JavaScript
- **codebase-summary.md**: Technical overview of the codebase
- **system-architecture.md**: Architecture diagram and component details
- **deployment-guide.md**: Instructions for deploying and maintaining the site
- **design-guidelines.md**: Visual identity and UX guidelines
- **api-reference.md**: Reference for external APIs and Jekyll features
- **summary.md**: Summary of the entire documentation suite

## Writing posts

Add new posts in `_posts/` using the `YYYY-MM-DD-title.md` format and include a
front‑matter title.

## Updating the role index

The Ansible role table in `index.md` is auto-generated from
`_data/ansible_roles.yml`.

### Adding a new role

```bash
python scripts/update_roles.py add role_name
```

### Removing a role

```bash
python scripts/update_roles.py remove role_name
```

### Listing all roles

```bash
python scripts/update_roles.py list
```

### Syncing roles from GitHub

```bash
python scripts/update_roles.py sync
```

This syncs public `buluma/ansible-role-*` repositories into the role list and
skips archived repositories. The **Update Ansible roles** workflow runs daily
or can be started manually from the Actions tab; it opens or updates a PR for
the generated change.

The workflow needs a repository secret named `ROLE_SYNC_TOKEN`: a fine-grained
token with **Contents: read and write** and **Pull requests: read and write**
access to this repository. The token lets the generated PR trigger the normal
PR CI workflow.

The table is automatically regenerated when the site builds. No manual editing
of `index.md` is needed for role changes.

## Local preview

If you want to preview the site locally:

1. Install Ruby + Bundler
2. Run `bundle install`
3. Run `bundle exec jekyll serve`
4. Visit `http://localhost:4000`

## Contributing

See `docs/CONTRIBUTING.md`.
