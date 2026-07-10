---
layout: default
title: "Tests"
---

# [Tests](#tests)

The filosofy to test is:
- Test multiple distributions.
- Test multiple version of Ansible, previous, current and next previous and future.

Each role's [GitHub Actions](https://github.com/features/actions) workflow runs [Molecule](https://molecule.readthedocs.io/en/stable/) across this set of distributions:

| Distribution        | Ansible 2.9 | Ansible 2.10 | Ansible devel |
|---------------------|-------------|--------------|---------------|
| Alpine latest       | yes         | yes          | yes           |
| Alpine edge         | yes         | yes          | yes           |
| Archlinux (base)    | yes         | yes          | yes           |
| CentOS 7            | yes         | yes          | yes           |
| CentOS latest       | yes         | yes          | yes           |
| Debian stable       | yes         | yes          | yes           |
| Debian latest       | yes         | yes          | yes           |
| Debian unstable     | yes         | yes          | yes           |
| Fedora latest       | yes         | yes          | yes           |
| Fedora rawhide      | yes         | yes          | yes           |
| OpenSuse Leap       | yes         | yes          | yes           |
| OpenSuse Tumbleweed | yes         | yes          | yes           |
| Ubuntu Artful (17)  | yes         | yes          | yes           |
| Ubuntu latest       | yes         | yes          | yes           |
| Ubuntu devel        | yes         | yes          | yes           |

There are multiple tests configured, here is how they relate.

## [Unit tests](#unit-tests)

To test an Ansible role, GitHub Actions runs Molecule on every commit and pull request. This verifies that the role does it's job, but does not ensure that it works in combination with other roles.

### [Time based unit tests](#time-based-unit-tests)

Because distributions, molecule, and ansible change over time, each role's workflow also carries a monthly cron schedule, staggered across the month so all ~240 roles aren't rebuilt on the same day. See the `schedule:` block in a role's `.github/workflows/molecule.yml` for its day.

