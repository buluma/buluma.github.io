# Contributing

Thanks for contributing to **buluma.github.io**. This repo contains the Buluma site content (pages, posts, and Ansible role index).

## Getting started

1. Fork the repo and create a branch: `git checkout -b my-change`
2. Make your changes (content, posts, or docs)
3. Preview locally if needed
4. Open a pull request with a clear description

## Content guidelines

- Keep posts concise and practical.
- Prefer real examples over theory.
- Use clear titles and dates in `_posts/`.
- Keep markdown readable and consistent with existing posts.

## Updating the roles index

If you update `index.md`, keep the roles table in this format:

```
|Role name|GitHub Action|Version|Downloads|
|---------|-------------|-------|---------|
|[role](https://galaxy.ansible.com/buluma/role)|[![github](...)](...)|[![version](...)](...)|[![downloads](...)](...)|
```

If you’re adding/removing many roles, update the list consistently and keep it sorted.

## Code of conduct

By participating, you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
