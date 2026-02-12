---
title: ansible-core 2.20 porting changes that matter in daily playbooks
---

# ansible-core 2.20 porting changes that matter in daily playbooks

In the last six months (Aug 2025–Feb 2026), **ansible-core 2.20** landed with a set of behavioral changes that are easy to miss but can impact real-world automation. The porting guide is the fastest way to spot those changes before they bite you in CI.

## Changes you’ll actually feel

### PowerShell path handling on Windows
Quote stripping in PowerShell operations has been removed. If you had playbooks that relied on Ansible “fixing” over‑quoted paths, you now need to tighten those paths yourself. This mostly affects Windows copy/fetch workflows.

### Deprecated features that are now gone
Several deprecated behaviors have been removed, including:
- The `smart` value for `DEFAULT_TRANSPORT`
- The v2 Galaxy server API in `ansible-galaxy`
- Deprecated options like `install_repoquery` in `dnf/dnf5` and `keepcache` in `yum_repository`
- Old Paramiko config keys and a few utility/compat shims

### Deprecation signal you should act on
`INJECT_FACTS_AS_VARS` is now deprecated, which is a strong hint to avoid depending on injected facts as top-level vars and instead use `ansible_facts` directly.

## Why it helps fellow developers

These changes make playbooks and plugins **more explicit and less magical**:
- Better Windows path hygiene improves cross‑shell reliability.
- Removing old APIs reduces “it works on my box” surprises across teams.
- Cleaner fact usage makes roles easier to reason about and test.

## Practical action list

1. **Run the porting guide checklist** against your Windows-heavy roles.
2. **Search for deprecated options** (`DEFAULT_TRANSPORT=smart`, `vaultid`, `install_repoquery`, `keepcache`) and replace or remove them.
3. **Refactor fact usage** to rely on `ansible_facts` instead of injected vars.

If you’re maintaining shared roles, updating now saves you a lot of churn once collections start tightening compatibility on top of 2.20.
