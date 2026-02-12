---
title: Molecule 5.0 makes CI more stable for roles
---

# Molecule 5.0 makes CI more stable for roles

If you run Molecule in CI, the last six months have brought improvements that make pipelines more stable. Molecule 5.0 reduces surprises around driver behavior and keeps scenarios more consistent across environments. citeturn5view2

## What changed

### Cleaner defaults
Molecule 5.0 is more opinionated about defaults, which reduces the need for custom glue in every repo. That makes CI definitions smaller and easier to maintain. citeturn5view2

### Better multi‑driver reliability
For teams that test on more than one platform, consistency across drivers is the most noticeable improvement. Fewer driver‑specific hacks are needed. citeturn5view2

## Why it helps fellow developers

- Less CI flakiness
- Faster contributor onboarding
- More confidence in release pipelines

## Practical action list

1. Standardize Molecule configs across repos.
2. Keep driver configs explicit but minimal.
3. Run Molecule locally with the same driver versions as CI.

Molecule 5.0 reduces friction in the feedback loop, which is exactly what teams want from testing.
