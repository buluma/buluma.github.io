---
title: Ways to include roles in roles
---

# Different methods to include roles

There are several ways to include roles from playbooks or roles.

### Classic
The [classic](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html) way:

<!-- TODO: Change to local -->
```yaml
---
- name: Build a machine
  hosts: all

  roles:
    - buluma.bootstrap
    - buluma.java
    - buluma.tomcat
```

Or a variation that allows per-role variables:

<!-- TODO: Change to local -->
```yaml
---
- name: Build a machine
  hosts: all

  roles:
    - role: buluma.bootstrap
    - role: buluma.java
      vars: java_version: 9
    - role: buluma.tomcat
```

### Include role

The [include_role](https://docs.ansible.com/ansible/latest/modules/include_role_module.html) way:

```yaml
---
- name: Build a machine
  hosts: all

  tasks:
    - name: include bootstrap
      include_role:
        name: buluma.bootstrap

    - name: include java
      include_role:
        name: buluma.java

    - name: include tomcat
      include_role:
        name: buluma.tomcat
```

Or a [with_items](https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html) (since [Ansible 2.3](https://github.com/ansible/ansible/issues/17966)) variation:
<!-- TODO: Change to local -->

```yaml
---
- name: Build a machine
  hosts: all

  tasks:
    - name: include role
      include_role:
        name: "{{ item }}"
      with_items:
        - buluma.bootstrap
        - buluma.java
        - buluma.tomcat
```

Sometimes it can be required to call one role from another role. I'd personally use import_role like this:

```yaml
---
- name: do something
  debug:
    msg: "Some task"

- name: call another role
  import_role:
    name: role.name
```

If the role (role.name in this example) requires variables, you can set them in `vars/main.yml`, like so:

```yaml
variable_x_for_role_name: foo
variable_y_for_role_name: bar
```

A real life example is my [buluma.artifactory](https://galaxy.ansible.com/buluma/artifactory) role calls [buluma.service](https://galaxy.ansible.com/buluma/service) role to add a service.
The code for [the artifactory role](https://github.com/buluma/ansible-role-artifactory/blob/master/tasks/main.yml) contains:
<!-- TODO: Change to local -->

```yaml
# snippet
- name: create artifactory service
  import_role:
    name: buluma.service
# endsnippet
```

and the variable are set in `[vars/main.yml](https://github.com/buluma/ansible-role-artifactory/blob/master/vars/main.yml)` contains:

```yaml
service_list:
  - name: artifactory
    description: Start script for Artifactory
    start_command: "{{ artifactory_home }}/bin/artifactory.sh start"
    stop_command: "{{ artifactory_home }}/bin/artifactory.sh stop"
    type: forking
    status_pattern: artifactory
```
