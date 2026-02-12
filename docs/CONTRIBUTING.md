# Contributing to buluma.github.io

Thank you for your interest in contributing to the buluma.github.io repository! This document outlines the process for contributing to this project.

## Table of Contents
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Making Changes](#making-changes)
- [Content Guidelines](#content-guidelines)
- [Technical Requirements](#technical-requirements)
- [Submitting Changes](#submitting-changes)
- [Style Guide](#style-guide)

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/buluma.github.io.git
   cd buluma.github.io
   ```
3. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Project Structure

```
buluma.github.io/
├── _includes/          # Jekyll includes
├── _layouts/           # Jekyll layouts
├── _posts/             # Blog posts
├── _sass/              # Sass stylesheets
├── assets/             # Static assets
├── docs/               # Documentation (including this file)
├── .github/            # GitHub Actions workflows
├── _config.yml         # Jekyll configuration
├── Gemfile             # Ruby dependencies
├── index.md            # Main landing page
└── ...
```

## Making Changes

### Content Updates
- Update the `index.md` file to add or modify Ansible role entries
- Add new blog posts in the `_posts/` directory
- Update documentation in the `docs/` directory

### Documentation Updates
- Follow the existing documentation structure
- Update the `docs/summary.md` file if adding new documentation
- Ensure all documentation is clear and accurate

### Code Changes
- Follow the coding standards outlined in `docs/code-standards.md`
- Test changes locally before submitting
- Ensure all links remain functional

## Content Guidelines

### Ansible Role Entries
- Keep the table in `index.md` sorted alphabetically by role name
- Ensure all badges are functional and point to the correct resources
- Verify that all links to Ansible Galaxy and GitHub repositories are correct
- Include accurate version and download information

### Documentation
- Write in clear, concise language
- Use proper Markdown formatting
- Include examples where helpful
- Cross-reference related documentation when appropriate

## Technical Requirements

### Local Development Environment
- Ruby 2.5 or higher
- Bundler gem
- Jekyll 4.x

### Setup
```bash
# Install dependencies
bundle install

# Run the site locally
bundle exec jekyll serve
```

### Testing
- Verify the site builds without errors
- Check that all links are functional
- Ensure the site is responsive on different screen sizes
- Validate that all badges display correctly

## Submitting Changes

1. Commit your changes with a descriptive message:
   ```bash
   git add .
   git commit -m "Add new Ansible role to index table"
   ```

2. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Open a pull request on GitHub with:
   - A clear title and description
   - Explanation of the changes made
   - Any relevant issue numbers

## Style Guide

### Markdown
- Use sentence case for headers
- Include alt text for all images
- Use relative links for internal references
- Follow the formatting standards in `docs/code-standards.md`

### Commit Messages
- Use imperative mood ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Include a blank line before longer descriptions
- Reference issues when applicable

### Pull Requests
- Keep pull requests focused on a single issue or feature
- Include tests for new functionality
- Update documentation as needed
- Ensure all checks pass before requesting review

## Questions?

If you have questions about contributing, feel free to open an issue in the repository for discussion.

Thank you for contributing to the buluma.github.io project!