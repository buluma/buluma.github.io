---
layout: default
title: Ansible Roles
---

## [Ansible Roles](#ansible-roles)

These [Ansible](https://www.ansible.com/) roles are
[simple in style](style.html) and [work well](how-to-use-these-roles.html)
together on many distributions and many Ansible version.

## [Unit tests](#unit-tests)

A monthly test to see of the role still works on the current distributions. Some
roles contain a version that requires frequent changes and tests. To better
understand what distributions and their versions are tested, have a look at the
[relations](relations.html) page.

| Role name                                                  | GitHub Action                                                                                                                                                                             | Version                                                                                                                                                         | Downloads                                                                                                             |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| {% for role in site.data.ansible_roles %}                  |                                                                                                                                                                                           |                                                                                                                                                                 |                                                                                                                       |
| [{{ role }}](https://galaxy.ansible.com/buluma/{{ role }}) | [![github](https://github.com/buluma/ansible-role-{{ role }}/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/ansible-role-{{ role }}/actions/workflows/molecule.yml) | [![version](https://img.shields.io/github/commits-since/buluma/ansible-role-{{ role }}/latest.svg)](https://github.com/buluma/ansible-role-{{ role }}/releases) | [![downloads](https://img.shields.io/ansible/role/d/buluma/{{ role }})](https://galaxy.ansible.com/buluma/{{ role }}) |
| {% endfor %}                                               |                                                                                                                                                                                           |                                                                                                                                                                 |                                                                                                                       |
