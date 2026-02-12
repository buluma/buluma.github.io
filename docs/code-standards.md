# Code Standards

## Markdown Standards

### Headers
- Use ATX-style headers with proper hierarchy
- Use proper capitalization (sentence case)
- Add anchor links for all headers

```markdown
## [Header Title](#header-title)

### [Sub Header](#sub-header)
```

### Tables
- Use proper table formatting with headers
- Align columns appropriately
- Use descriptive column headers

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
```

### Links
- Use relative links for internal pages
- Use absolute links for external resources
- Always include descriptive link text

## Jekyll Standards

### Front Matter
- Include proper YAML front matter for all pages
- Use consistent variable names
- Document all custom variables

```yaml
---
title: Page Title
description: Brief description of the page
---
```

### Includes
- Use includes for reusable components
- Name includes descriptively with leading underscore
- Keep includes focused on single responsibilities

### Layouts
- Follow the default layout pattern
- Use consistent structure across layouts
- Include proper SEO tags

## HTML Standards

### Accessibility
- Use semantic HTML elements
- Include proper alt attributes for images
- Ensure proper heading hierarchy

### Formatting
- Use lowercase for all HTML tags
- Use double quotes for attribute values
- Indent consistently (2 spaces)

## CSS Standards

### Naming Convention
- Use BEM methodology for class names
- Use kebab-case for class names
- Prefix utility classes with `u-`

### Organization
- Organize CSS in logical sections
- Use meaningful comments
- Group related styles together

## JavaScript Standards

### Style Guide
- Follow Airbnb JavaScript Style Guide
- Use ES6+ features where appropriate
- Include proper error handling

### Organization
- Use modules for code organization
- Keep functions focused on single responsibilities
- Include JSDoc comments for complex functions