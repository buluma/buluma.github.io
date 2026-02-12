# API Reference

## Overview

The buluma.github.io site is a static Jekyll-based site that doesn't expose a traditional API. However, it integrates with several external services and APIs to provide dynamic information about Ansible roles.

## External API Integrations

### GitHub API
Used to fetch repository information and generate badges.

#### Endpoints Used
- `https://api.github.com/repos/buluma/{role_name}/actions/runs` - For GitHub Actions status badges
- `https://api.github.com/repos/buluma/{role_name}/releases/latest` - For version information

#### Rate Limits
- GitHub API rate limits apply (5000 requests per hour for authenticated requests)
- Unauthenticated requests are limited to 60 requests per hour

#### Authentication
- No authentication required for public repository information
- Public data only is accessed

### Ansible Galaxy API
Used to fetch role download statistics and other metadata.

#### Endpoints Used
- `https://galaxy.ansible.com/api/v1/roles/?owner__username=buluma&name={role_name}` - For role information
- `https://img.shields.io/ansible/role/d/buluma/{role_name}` - For download count badges

#### Rate Limits
- Subject to Galaxy API rate limits
- Cached responses may be used to reduce API calls

### GitLab API
Used to fetch CI status for roles hosted on GitLab.

#### Endpoints Used
- `https://gitlab.com/api/v4/projects/{project_id}/repository/branches/main` - For GitLab CI status
- `https://gitlab.com/shadowwalker/{role_name}/badges/main/pipeline.svg` - For pipeline status badges

## Badge APIs

### GitHub Actions Badge
```
https://github.com/buluma/{role_name}/actions/workflows/molecule.yml/badge.svg
```

#### Parameters
- `{role_name}`: Name of the Ansible role

#### Response
- SVG image showing workflow status
- Updates automatically when workflow status changes

### Download Count Badge
```
https://img.shields.io/ansible/role/d/buluma/{role_name}
```

#### Parameters
- `{role_name}`: Name of the Ansible role

#### Response
- SVG image showing download count
- Updates automatically based on Galaxy statistics

### Version Badge
```
https://img.shields.io/github/commits-since/buluma/{role_name}/latest.svg
```

#### Parameters
- `{role_name}`: Name of the Ansible role

#### Response
- SVG image showing version information
- Updates when new commits are made

## Jekyll Runtime API

### Liquid Filters
The site uses various Liquid filters provided by Jekyll and its plugins:

#### Standard Liquid Filters
- `date` - Format date values
- `escape` - Escape HTML entities
- `strip_html` - Remove HTML tags
- `truncate` - Limit string length

#### Jekyll-Specific Filters
- `relative_url` - Generate relative URLs
- `absolute_url` - Generate absolute URLs
- `slugify` - Convert to URL-safe string
- `xml_escape` - Escape XML entities

### Jekyll Variables
The site uses various Jekyll-provided variables:

#### Site Variables
- `site.title` - Site title from config
- `site.description` - Site description from config
- `site.github` - GitHub-specific variables
- `site.time` - Current build time

#### Page Variables
- `page.title` - Page title
- `page.content` - Page content
- `page.url` - Page URL

## Jekyll Plugins

### jekyll-seo-tag
Provides SEO optimization features:

#### Variables
- `page.title` - Used for title tag
- `page.description` - Used for meta description
- `page.image` - Used for social media images
- `site.author` - Used for author meta tags

### Custom Includes
The site implements custom includes for common elements:

#### Available Includes
- `head.html` - Head section content
- `header.html` - Header navigation
- `footer.html` - Footer content

## Data Formats

### Markdown
The site uses standard Markdown syntax with some Jekyll extensions:

#### Supported Elements
- Headers (#, ##, ###)
- Lists (ordered and unordered)
- Links and images
- Code blocks with syntax highlighting
- Tables

### YAML Front Matter
Each page may include YAML front matter:

```yaml
---
title: Page Title
description: Description of the page
layout: default
---
```

## Hooks and Extensions

### Build Hooks
The site uses standard Jekyll build hooks:
- `:post_write` - After site is written to disk
- `:post_render` - After pages are rendered

### Custom Configuration
The `_config.yml` file supports various Jekyll options:
- `plugins` - List of plugins to load
- `theme` - Jekyll theme to use
- `collections` - Custom content collections
- `defaults` - Default front matter values

## Integration Points

### GitHub Actions Workflow
The site is built and deployed via GitHub Actions with the following steps:
1. Checkout repository
2. Setup Ruby environment
3. Install dependencies
4. Build Jekyll site
5. Run HTML validation
6. Deploy to GitHub Pages

### HTML Validation
The site uses html-proofer to validate:
- Internal links
- External links
- HTML structure
- Image references