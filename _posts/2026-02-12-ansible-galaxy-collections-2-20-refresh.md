# Galaxy collections in 2026: what changed and why it helps

The last six months brought a quieter but important shift in **Ansible Galaxy workflows**: the older v2 Galaxy server API is gone in `ansible-galaxy`. If you had custom tooling that still talked to v2, it will now fail and needs to move to the supported API.

## What changed

### v2 API removed
The `ansible-galaxy` CLI no longer supports the v2 server API. That’s a hard break for legacy automation that scraped or pushed data using v2 endpoints.

### Cleaner, more predictable CLI behavior
Alongside API cleanup, a few legacy compat shims were removed. The net effect is fewer “it used to work” surprises and more deterministic behavior for automation pipelines.

## Why it helps other developers

When teams standardize on the supported Galaxy API, the pipeline becomes:
- **More stable** across Ansible versions.
- **Easier to maintain** because fewer undocumented behaviors remain.
- **More secure** because old endpoints are a common attack surface and often lack modern auth expectations.

## Quick migration checklist

1. **Inventory internal scripts** that call Galaxy directly.
2. **Check for v2 endpoints** and update to the supported API.
3. **Re-run collection publish workflows** in CI to confirm behavior.

This is a small change on paper, but it eliminates a class of flaky Galaxy automation that’s been around for years.
