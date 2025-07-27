# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A minimal personal website with integrated blog using no frameworks or build tools - just HTML, CSS, and a Python script for blog generation. Features professional typography (Inter + Charter), component-based architecture, and AI transparency tagging.

## Tech Stack

- **Frontend**: Hand-written HTML + CSS with Inter (headers) + Charter (body) fonts
- **Blog**: Markdown files converted to HTML via Python script with datetime sorting
- **Components**: Header component system using JavaScript for consistency
- **Branding**: Favicon and logo integration
- **Hosting**: GitHub Pages
- **Deployment**: GitHub Actions (automated on push to main)

## Project Structure

```
├── index.html              # Homepage with intro/work/writing/contact sections
├── blog.html              # Blog index (generated with AI tags)
├── about.html             # About page with background/interests
├── style.css              # Enhanced styles with typography and components
├── favicon.png            # Site favicon (red "i" design)
├── logo.png               # Navigation logo (black "i" design)
├── header.html            # Reusable header component
├── header.js              # Component loader script
├── posts/
│   ├── *.md               # Blog posts with enhanced frontmatter
│   └── *.html             # Generated HTML with proper navigation
├── generate_blog.py       # Enhanced blog generator with AI tagging
└── .github/workflows/
    └── deploy.yml         # Auto-deployment workflow
```

## Common Commands

### Blog Generation
```bash
# Generate blog locally (converts .md to .html, updates index, handles components)
python3 generate_blog.py

# Serve locally for testing
python3 -m http.server 8000
# Then visit http://localhost:8000
```

### Adding Content
```bash
# Create new blog post with enhanced frontmatter
# 1. Create posts/new-post.md with frontmatter including ai_assisted tag
# 2. Run python3 generate_blog.py to test locally
# 3. Commit and push - GitHub Actions handles deployment
```

## Blog Post Format

Blog posts use markdown with enhanced YAML frontmatter:

```markdown
---
title: "Post Title"
date: "2025-01-27 14:30"  # Full datetime for sorting (displays as date only)
excerpt: "Brief description for listings"
published: true
ai_assisted: false        # Transparency tagging for AI assistance
---

# Your Content Here

Standard markdown content...
```

## Key Features

### Component System
- **Header Component**: Edit `header.html` once, updates across all pages via `header.js`
- **Navigation**: Logo + name on left, links on right
- **Favicon**: Integrated across all pages and templates

### Typography & Design
- **Headers**: Inter font (600/500 weights) for clean, modern feel
- **Body**: Charter serif for excellent reading experience
- **Colors**: Custom red (#EB3349) for links and highlights
- **Layout**: Section-based organization with proper spacing

### Blog Features
- **AI Transparency**: Posts can be tagged as AI-assisted with subtle badges
- **DateTime Sorting**: Use full datetime in frontmatter for precise ordering
- **Recent Posts**: Homepage shows latest 3 posts automatically
- **Generated Content**: Blog index and homepage updated automatically

### Brand Integration
- **Logo**: Professional "i" logo that serves as clickable home link
- **Name**: "ignacio j semerene" displayed beside logo
- **Favicon**: Consistent branding across browser tabs

## Architecture Notes

- **No build process**: Files are served directly with minimal JavaScript
- **Component loading**: Header loads via fetch() for consistency without frameworks
- **Blog generation**: Python script handles markdown conversion and template updates
- **Styling**: Direct CSS editing with Google Fonts integration
- **Deployment**: GitHub Actions runs generator and deploys to Pages
- **URLs**: Uses .html extensions with proper relative linking

## Styling Guidelines

### Font Usage
- **Headers (h1, h2, h3, nav)**: Inter with appropriate weights
- **Body text**: Charter for readability
- **Code elements**: Inherit system fonts

### Color Scheme
- **Primary**: #EB3349 (links, highlights)
- **Text**: #1a202c (dark), #4a5568 (medium), #718096 (light)
- **Backgrounds**: Subtle grays for hover states and tags

### Component Classes
- **Navigation**: `.logo-link`, `.site-name`, `.nav-links`
- **AI Tags**: `.ai-tag` for transparency badges
- **Posts**: `.post-list`, `.post-date` for blog styling

## Key Files

- `generate_blog.py`: Enhanced blog generation with AI tagging and datetime support
- `style.css`: Complete styling with typography, components, and responsive design
- `header.html`: Single source of truth for site navigation
- `header.js`: Component loader for header consistency
- `index.html`: Homepage with section-based content organization
- `.github/workflows/deploy.yml`: Automated deployment pipeline

## Content Strategy

- **Homepage**: Intro → Work → Recent Writing → Contact flow
- **About**: Personal story, background, interests, contact
- **Blog**: Clean post listings with AI transparency where applicable
- **Navigation**: Minimal, logo-centric design with clear hierarchy