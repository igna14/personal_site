# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A minimal personal website with integrated blog using no frameworks or build tools - just HTML, CSS, and a Python script for blog generation.

## Tech Stack

- **Frontend**: Hand-written HTML + CSS
- **Blog**: Markdown files converted to HTML via Python script
- **Hosting**: GitHub Pages
- **Deployment**: GitHub Actions (automated on push to main)

## Project Structure

```
├── index.html              # Homepage
├── blog.html              # Blog index (generated)
├── about.html             # About page
├── style.css              # Global styles
├── posts/
│   ├── hello-world.md     # Blog posts in markdown
│   └── hello-world.html   # Generated HTML from markdown
├── generate_blog.py       # Blog generator script
└── .github/workflows/
    └── deploy.yml         # Auto-deployment workflow
```

## Common Commands

### Blog Generation
```bash
# Generate blog locally (converts .md to .html and updates index)
python generate_blog.py

# Serve locally for testing
python -m http.server 8000
# Then visit http://localhost:8000
```

### Adding Content
```bash
# Create new blog post
# 1. Create posts/new-post.md with frontmatter
# 2. Run python generate_blog.py to test locally
# 3. Commit and push - GitHub Actions handles deployment
```

## Blog Post Format

Blog posts use markdown with YAML frontmatter:

```markdown
---
title: "Post Title"
date: "2025-01-27"
excerpt: "Brief description for listings"
published: true
---

# Your Content Here

Standard markdown content...
```

## Architecture Notes

- **No build process**: Files are served directly
- **Blog generation**: Python script converts markdown to HTML and updates homepage
- **Styling**: Direct CSS editing, no preprocessors
- **Deployment**: GitHub Actions runs blog generator and deploys to Pages
- **URLs**: Uses .html extensions (can be removed via GitHub Pages configuration)

## Key Files

- `generate_blog.py`: Core blog generation logic, parses frontmatter and converts markdown
- `style.css`: All styling in a single file with simple, readable CSS
- `index.html`: Homepage template with placeholder for recent posts injection
- `.github/workflows/deploy.yml`: Automated deployment on push to main branch