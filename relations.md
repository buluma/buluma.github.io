---
layout: default
title: "Distribution relations"
---

# [Distribution relations](#distribution-relations)

There is a relation between:

- Ansible Platforms & Versions in `meta/main.yml`/`meta/preferences.yml` for a role.
- The [docker-molecule-images](https://github.com/buluma/docker-molecule-images) tag(s) that platform/version resolves to.
- The workflow file in that repo building each tag.

Since every role's CI now pulls test containers from the single `docker-molecule-images` repo (see [docker_builds.md](docker_builds.md)), the "Image" column below is always the same repo — what actually varies, and what this table exists to clarify, is which tag(s) a given Ansible platform/version resolves to. This mapping comes from [ansible-generator](https://github.com/buluma/ansible-generator)'s `vars/main.yml`, which drives CI generation for every role in this project.

|Ansible Platform|Platform Version|Image                 |Tag(s)                                              |Workflow file(s)                                                   |
|----------------|----------------|----------------------|-----------------------------------------------------|--------------------------------------------------------------------|
|Alpine|all|docker-molecule-images|alpine-openrc|alpine-openrc.yml|
|AlmaLinux|**all**|docker-molecule-images|almalinux10, almalinux9|almalinux10.yml, almalinux9.yml|
|AlmaLinux|10|docker-molecule-images|almalinux10|almalinux10.yml|
|AlmaLinux|9|docker-molecule-images|almalinux9|almalinux9.yml|
|Amazon|all|docker-molecule-images|amazonlinux2023|amazonlinux2023.yml|
|Amazon|2023|docker-molecule-images|amazonlinux2023|amazonlinux2023.yml|
|Archlinux|all|docker-molecule-images|archlinux|archlinux.yml|
|Debian|**all**|docker-molecule-images|debian13, debian12|debian13.yml, debian12.yml|
|Debian|trixie|docker-molecule-images|debian13|debian13.yml|
|Debian|bookworm|docker-molecule-images|debian12|debian12.yml|
|Debian|bullseye|docker-molecule-images|debian11|debian11.yml|
|Debian|13|docker-molecule-images|debian13|debian13.yml|
|Debian|12|docker-molecule-images|debian12|debian12.yml|
|Debian|11|docker-molecule-images|debian11|debian11.yml|
|EL|**all**|docker-molecule-images|rockylinux10, almalinux10, rockylinux9, almalinux9|rockylinux10.yml, almalinux10.yml, rockylinux9.yml, almalinux9.yml|
|EL|**10**|docker-molecule-images|rockylinux10, almalinux10|rockylinux10.yml, almalinux10.yml|
|EL|**9**|docker-molecule-images|rockylinux9, almalinux9|rockylinux9.yml, almalinux9.yml|
|Fedora|**all**|docker-molecule-images|fedora44, fedora43, fedora42|fedora44.yml, fedora43.yml, fedora42.yml|
|Fedora|42|docker-molecule-images|fedora42|fedora42.yml|
|Fedora|43|docker-molecule-images|fedora43|fedora43.yml|
|Fedora|44|docker-molecule-images|fedora44|fedora44.yml|
|Kali|all|docker-molecule-images|kalilinux|kalilinux.yml|
|openSUSE|**all**|docker-molecule-images|opensuse, opensuse-tumbleweed|opensuse.yml, opensuse-tumbleweed.yml|
|openSUSE|16.0|docker-molecule-images|opensuse|opensuse.yml|
|openSUSE|tumbleweed|docker-molecule-images|opensuse-tumbleweed|opensuse-tumbleweed.yml|
|OracleLinux|**all**|docker-molecule-images|oraclelinux10, oraclelinux9, oraclelinux8|oraclelinux10.yml, oraclelinux9.yml, oraclelinux8.yml|
|OracleLinux|10|docker-molecule-images|oraclelinux10|oraclelinux10.yml|
|OracleLinux|9|docker-molecule-images|oraclelinux9|oraclelinux9.yml|
|OracleLinux|8|docker-molecule-images|oraclelinux8|oraclelinux8.yml|
|Rocky|**all**|docker-molecule-images|rockylinux10, rockylinux9|rockylinux10.yml, rockylinux9.yml|
|Rocky|9|docker-molecule-images|rockylinux9|rockylinux9.yml|
|Rocky|10|docker-molecule-images|rockylinux10|rockylinux10.yml|
|Ubuntu|**all**|docker-molecule-images|ubuntu2604, ubuntu2404, ubuntu2204|ubuntu2604.yml, ubuntu2404.yml, ubuntu2204.yml|
|Ubuntu|resolute|docker-molecule-images|ubuntu2604|ubuntu2604.yml|
|Ubuntu|noble|docker-molecule-images|ubuntu2404|ubuntu2404.yml|
|Ubuntu|jammy|docker-molecule-images|ubuntu2204|ubuntu2204.yml|
|Ubuntu|focal|docker-molecule-images|ubuntu2004|ubuntu2004.yml|
|Ubuntu|bionic|docker-molecule-images|ubuntu1804|ubuntu1804.yml|
|Ubuntu|26.04|docker-molecule-images|ubuntu2604|ubuntu2604.yml|
|Ubuntu|24.04|docker-molecule-images|ubuntu2404|ubuntu2404.yml|
|Ubuntu|22.04|docker-molecule-images|ubuntu2204|ubuntu2204.yml|
|Ubuntu|20.04|docker-molecule-images|ubuntu2004|ubuntu2004.yml|
|Ubuntu|18.04|docker-molecule-images|ubuntu1804|ubuntu1804.yml|

All **bold** printed items require some kind of attention. This could mean:

- A single Ansible Galaxy Platform Version resolves to multiple Docker tags (EL, Rocky's `all`, Debian's `all`, AlmaLinux's `all`, openSUSE's `all`, OracleLinux's `all`, Fedora's `all`, Ubuntu's `all`) — each tag gets its own molecule job in the generated CI matrix.
- `EL` in particular always tests against both Rocky Linux and AlmaLinux for a given major version (EL 9 -> both `rockylinux9` and `almalinux9`), since it represents the RHEL-compatible family generically rather than one specific distro.

A few gaps worth knowing about:

- **SLES is intentionally unsupported.** `sles12`/`sles15` exist in docker-molecule-images but require a paid SUSE subscription to pull the base image, so CI on that platform could never go green without credentials this project doesn't have.
- **Fedora 45 is excluded from `all`.** It tracks Rawhide, which currently ships Python 3.15.0b3 — that version's `dataclasses` module dropped `_is_type`, breaking ansible-core's AnsiballZ module wrapper.
- **Debian 11 (bullseye) dropped from `all`.** The version-support policy tests only the latest 3 releases per distro; Debian is now at 12/13, so 11 is only available as an explicit pin, not the default.
