---
layout: default
title: Ansible Roles
nav_order: 1
---

# Ansible Roles

These [Ansible](https://www.ansible.com/) roles are
[simple in style](style.html) and [work well](how-to-use-these-roles.html)
together on many distributions and many Ansible versions.

## Unit Tests

A monthly test to see if the role still works on the current distributions. Some
roles contain a version that requires frequent changes and tests. To better
understand what distributions and their versions are tested, have a look at the
[relations](relations.html) page.

## All Roles ({{ site.data.ansible_roles | size }})

{% assign roles = site.data.ansible_roles | sort %}

| Role | Galaxy | CI | Version | Downloads |
|------|--------|-----|---------|-----------|
{% for role in roles %}
| [`{{ role }}`](https://galaxy.ansible.com/buluma/{{ role }}) | [![Galaxy](https://img.shields.io/badge/galaxy-{{ role }}-brightgreen?logo=ansible)](https://galaxy.ansible.com/buluma/{{ role }}) | [![CI](https://github.com/buluma/ansible-role-{{ role }}/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/ansible-role-{{ role }}/actions/workflows/molecule.yml) | [![Version](https://img.shields.io/github/commits-since/buluma/ansible-role-{{ role }}/latest.svg)](https://github.com/buluma/ansible-role-{{ role }}/releases) | [![Downloads](https://img.shields.io/ansible/role/d/buluma/{{ role }})](https://galaxy.ansible.com/buluma/{{ role }}) |
{% endfor %}
