# Deployment Guide

## Overview

This guide explains how to deploy and maintain the buluma.github.io site on GitHub Pages.

## Prerequisites

- GitHub account with repository access
- Ruby 2.5+ installed (for local development)
- Bundler gem installed
- Git client

## Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/buluma/buluma.github.io.git
cd buluma.github.io
```

### 2. Install Dependencies
```bash
gem install bundler
bundle install
```

### 3. Run Local Server
```bash
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`

## GitHub Pages Deployment

### Automatic Deployment
The site is automatically deployed when changes are pushed to the `main` branch. GitHub Actions handles the build and deployment process.

### GitHub Actions Workflow
The deployment workflow is defined in `.github/workflows/ci.yml` and includes:
1. Checking out the repository
2. Setting up Ruby environment
3. Installing dependencies
4. Building the Jekyll site
5. Running HTML validation
6. Publishing to GitHub Pages

## Configuration

### Jekyll Configuration
The `_config.yml` file contains site-wide settings:
- Site title and description
- Theme settings
- SEO configuration
- Plugin settings

### GitHub Pages Settings
In the repository settings:
- Source: Deploy from a branch
- Branch: `main`
- Workflow handles the build process

## Troubleshooting

### Common Issues

#### Ruby Dependency Issues
If experiencing Ruby dependency issues:
1. Update your Ruby version to match the requirements
2. Run `bundle install` to install correct gem versions
3. Check for compatibility issues with newer Ruby versions

#### Build Failures
If the site fails to build:
1. Check the GitHub Actions logs for error details
2. Verify all links are valid
3. Ensure YAML frontmatter is properly formatted
4. Run `bundle exec jekyll build` locally to reproduce

#### Link Validation Errors
If HTML validation fails:
1. Check for broken external links
2. Verify internal links point to existing pages
3. Update any outdated URLs

## Maintenance Tasks

### Regular Maintenance
- Update dependencies periodically with `bundle update`
- Verify all external links still work
- Refresh content to reflect current Ansible roles
- Monitor GitHub Actions for build failures

### Content Updates
1. Update the roles table in `index.md` with new roles
2. Update download counts and version information
3. Verify all badges are still functional
4. Test the site locally before pushing

### Security Updates
- Keep Ruby and gems updated
- Monitor for security advisories
- Update dependencies when security patches are released

## Performance Optimization

### Image Optimization
- Compress images before adding to the repository
- Use appropriate formats (WebP where supported)
- Minimize file sizes without sacrificing quality

### Asset Optimization
- Minify CSS and JavaScript
- Leverage browser caching
- Use efficient Jekyll plugins

## Backup Strategy

### Repository Backup
- GitHub automatically backs up the repository
- Clone the repository regularly to local storage
- Consider mirroring to another Git hosting service

### Content Backup
- Maintain a local copy of all content
- Export important data periodically
- Document any custom configurations

## Rollback Procedures

### If Deployment Fails
1. Identify the commit that caused the issue
2. Create a hotfix branch from the previous working commit
3. Apply necessary fixes
4. Merge to main to trigger a new deployment

### Using Git to Revert Changes
```bash
# Find the commit hash before the problematic changes
git log --oneline

# Create a new branch from the good commit
git checkout -b hotfix-rollback <good-commit-hash>

# Cherry-pick any good changes after the problematic commit
git cherry-pick <good-commit-hash>

# Push and create a pull request
git push origin hotfix-rollback
```

## Monitoring

### GitHub Actions
Monitor the Actions tab for:
- Build failures
- Performance degradation
- Dependency issues

### GitHub Pages
Check the Pages tab for:
- Deployment status
- SSL certificate status
- Traffic analytics