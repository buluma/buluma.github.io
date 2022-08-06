---
title: GitHub action to run Molecule
---

# GitHub action to run Molecule

[GitHub Actions](https://github.com/features/actions) is an approach to offering CI, using other peoples actions from the [GitHub Action Marketplace](https://github.com/marketplace?type=actions).

The intent is to let a developer of an Action think about 'hard stuff' and the user of an action simply include another step into a workflow.

So; I wrote a GitHub action to test an Ansible role with a single action.

## Using the GitHub Action.
<!-- TODO: change to local -->
Have a look at the [Molecule action](https://github.com/marketplace/actions/test-ansible-roles-with-molecule).

It boils down to adding this snippet to `.github/workflows/molecule.yml`:

```yaml
---
on:
  - push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: checkout
        uses: actions/checkout@v3
        with:
          path: "${{ github.repository }}"
      - name: molecule
        uses: buluma/molecule-action@master
```

## How it works

You may want to write your own action, here is an overview of the required components.

```
+--- Repository with an Ansible role ---+
| - .github/workflows/molecule.yml      |
+-+-------------------------------------+
  |
  |    +-------- buluma/molecule-action --------+
  +--> | - image: buluma/github-action-molecule |
       +-+--------------------------------------------+
         |
         |    +--- github-action-molecule ---+
         +--> | - pip install molecule       |
              | - pip install tox            |
              +------------------------------+
```

### 1. Create a container
<!-- TODO: change to local -->
First create a container that has all tools installed you need and push it to [Docker Hub](https://hub.docker.com/repository/docker/buluma/github-action-molecule/). Here is the [code for my container](https://github.com/buluma/docker-github-action-molecule)

### 2. Create an action
<!-- TODO: change to local -->
Create a [GitHub repository per action](https://github.com/buluma/molecule-action). It should at least contain an `action.yml`. Have a look at [the documentation for Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/building-actions).

### 3. Integrate your action

Pick a repository, and add a file (likely with the name of the action) in `.gitlab/workflows/my_action.yml`. The contents should refer to the action:

```yaml
    steps:
      - name: checkout
        uses: actions/checkout@v3
        with:
          path: "${{ github.repository }}"
      - name: molecule
        uses: buluma/molecule-action@master
        with:
          image: ${{ matrix.image }}
```
<!-- TODO: change to local -->
[A full example here](https://github.com/buluma/ansible-role-squid/blob/master/.github/workflows/molecule.yml).

The benefit is that you (or others) can reuse the action. Have fun making GitHub actions!
