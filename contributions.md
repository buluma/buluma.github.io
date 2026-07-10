---
layout: default
title: Contributions
---

## Ansible roles contributions status

Here is an overview of all issues and pull requests per role.

{% assign roles = site.data.ansible_roles | sort %}

|Role|Issues|Pull requests|
|----|------|--------------|
{% for role in roles %}|[{{ role }}](https://galaxy.ansible.com/buluma/{{ role }})|[![issues](https://img.shields.io/github/issues-raw/buluma/ansible-role-{{ role }})](https://github.com/buluma/ansible-role-{{ role }}/issues)|[![pull requests](https://img.shields.io/github/issues-pr/buluma/ansible-role-{{ role }})](https://github.com/buluma/ansible-role-{{ role }}/pulls)|
{% endfor %}
