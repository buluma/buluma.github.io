---
title: Terraform 1.10 config-driven import and why it matters
author: buluma
categories:
  - terraform
  - ci-cd
  - testing
  - best-practices
  - devops
---



# Terraform 1.10 config-driven import and why it matters

Terraform 1.10 introduced **config‑driven import**, and in the past six months it has matured into a practical workflow for teams managing brownfield infrastructure. Instead of writing ad-hoc CLI scripts, you can declare import blocks in configuration and let Terraform reconcile resources in a repeatable way.

## What changed

### Import is now part of configuration
You can define import blocks in `.tf` files, commit them, and run `terraform apply` to bring existing infrastructure under management. This makes imports reviewable and repeatable.

### Safer migration workflows
Because the import intent lives in version control, code review becomes the safety net. Teams can see *exactly* what is being imported and why.

## Why it helps fellow developers

This shifts import from “hero debugging” to a **team‑friendly workflow**:
- Less tribal knowledge about IDs and one-off commands
- Easier rollback and review
- Better alignment with IaC best practices

## Practical action list

1. Use import blocks for any existing infra being adopted into Terraform.
2. Keep import blocks alongside the resources they target.
3. Remove import blocks after successful state adoption.

It’s a small feature that makes the “from legacy to IaC” path way smoother.
