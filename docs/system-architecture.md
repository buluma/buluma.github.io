# System Architecture

## Overview

The buluma.github.io site is a static Jekyll-based website hosted on GitHub Pages. It serves as a documentation portal for Ansible roles developed by the buluma community.

## Architecture Diagram

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Author        │───▶│   GitHub Repo    │───▶│   GitHub Pages  │
│   (Markdown)    │    │   (Jekyll)       │    │   (Static Site) │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │   Jekyll Build   │
                       │   Process        │
                       └──────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │   HTML Validation│
                       │   (html-proofer) │
                       └──────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │   Deployment     │
                       │   (GitHub Pages) │
                       └──────────────────┘
```

## Components

### 1. Content Layer
- **Markdown files**: Store documentation content
- **YAML frontmatter**: Configure page-specific settings
- **Tables**: Display role information in structured format

### 2. Presentation Layer
- **Jekyll Theme**: Hacker theme provides styling
- **SASS**: Custom styling and theme modifications
- **Layouts**: Define page structure
- **Includes**: Reusable components

### 3. Build Layer
- **Jekyll Engine**: Static site generator
- **Ruby Dependencies**: Gems required for site generation
- **Plugins**: SEO, sitemap, and other functionality

### 4. Deployment Layer
- **GitHub Actions**: CI/CD pipeline
- **GitHub Pages**: Static hosting service
- **CDN**: Global content delivery

## Data Flow

1. **Content Creation**: Authors create/update Markdown files
2. **Jekyll Processing**: Jekyll transforms Markdown to HTML
3. **Asset Compilation**: Sass is compiled to CSS
4. **Validation**: HTML proofer validates links and structure
5. **Deployment**: GitHub Pages serves the static site

## Technology Stack

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Styling with Sass preprocessing
- **Markdown**: Content authoring format

### Backend
- **Jekyll**: Static site generator
- **Ruby**: Runtime environment
- **Liquid**: Template language

### Infrastructure
- **GitHub Pages**: Hosting platform
- **GitHub Actions**: CI/CD pipeline
- **CDN**: Content delivery

## Integration Points

### External Services
- **GitHub**: Repository hosting and Actions
- **Galaxy.ansible.com**: Role download statistics
- **Img.shields.io**: Badge generation
- **GitLab**: CI status for some roles

### Internal Components
- **_config.yml**: Site-wide configuration
- **Gemfile**: Ruby dependencies
- **.github/workflows/**: CI/CD configuration

## Security Considerations

- Static site reduces attack vectors
- No server-side processing
- Content delivered over HTTPS
- No user input processing
- No database connections

## Performance Characteristics

- Fast loading due to static nature
- CDN distribution for global access
- Minimal external dependencies
- Optimized for GitHub Pages hosting