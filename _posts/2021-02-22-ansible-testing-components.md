---
title: Ansible testing components
---

# Ansible testing components

To test Ansible, I use quite a number of components. This page lists the components uses, their versions, and where they are used.

|Component             |Used   |Latest |Used where                            |
|----------------------|-------|-------|--------------------------------------|
|ansible               |2.9    |2.9.18 |tox.ini                               |
|ansible               |2.10   |2.10.7 |tox.ini                               |
|molecule              |>=3,<4 |![c][c]|docker-github-action-molecule         |
|tox                   |latest |n.a.   |docker-github-action-molecule         |
|ansible-lint          |latest |![e][e]|docker-github-action-molecule         |
|pre-commit            |2.9.3  |v2.10.1|installed on development desktop.      |
|molecule-action       |2.6.16 |![g][g]|.github/workflows/molecule.yml        |
|github-action-molecule|3.0.6  |![h][h]|.gitlab-ci.yml                        |
|ubuntu                |20.04  |20.04  |.github/workflows/galaxy.yml          |
|ubuntu                |20.04  |20.04  |.github/workflows/molecule.yml        |
|ubuntu                |20.04  |20.04  |.github/workflows/requirements2png.yml|
|ubuntu                |20.04  |20.04  |.github/workflows/todo.yml            |
|galaxy-action         |1.1.0  |![m][m]|.github/workflows/galaxy.yml          |
|graphviz-action       |1.0.7  |![n][n]|.github/workflows/requirements2png.yml|
|checkout              |v2     |![o][o]|.github/workflows/requirements2png.yml|
|checkout              |v2     |![o][o]|.github/workflows/molecule.yml        |
|todo-to-issue         |v2.3   |![p][p]|.github/workdlows/todo.yml            |
|python                |3.9    |3.9    |.travis.yml                           |
|pre-commit-hooks      |v3.4.0 |![r][r]|.pre-commit-config.yaml               |
|yamllint              |v1.26.0|v1.26.0|.pre-commit-config.yaml               |
|my pre-commit         |v1.4.5 |![u][u]|.pre-commit-config.yaml               |
|fedora                |33     |33     |docker-github-action-molecule         |

[c]: https://img.shields.io/pypi/v/molecule
[e]: https://img.shields.io/github/v/release/ansible-community/ansible-lint
[g]: https://img.shields.io/github/v/release/buluma/molecule-action
[h]: https://img.shields.io/github/v/release/buluma/docker-github-action-molecule
[m]: https://img.shields.io/github/v/release/buluma/galaxy-action
[n]: https://img.shields.io/github/v/release/buluma/graphviz-action
[o]: https://img.shields.io/github/v/release/actions/checkout
[p]: https://img.shields.io/github/v/release/alstr/todo-to-issue-action
[r]: https://img.shields.io/github/v/release/pre-commit/pre-commit-hooks
[u]: https://img.shields.io/github/v/release/buluma/pre-commit
