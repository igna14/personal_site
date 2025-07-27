#!/usr/bin/env python3
import re
from datetime import datetime
from pathlib import Path

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown"""
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    frontmatter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip().strip('"\'')
    
    return frontmatter, parts[2].strip()

def markdown_to_html(content):
    """Basic markdown conversion"""
    # Headers
    content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    
    # Bold and italic
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
    
    # Code blocks
    content = re.sub(r'```(.+?)```', r'<pre><code>\1</code></pre>', content, flags=re.DOTALL)
    content = re.sub(r'`(.+?)`', r'<code>\1</code>', content)
    
    # Paragraphs
    paragraphs = content.split('\n\n')
    html_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<'):
            p = f'<p>{p}</p>'
        html_paragraphs.append(p)
    
    return '\n\n'.join(html_paragraphs)

def generate_blog():
    """Generate HTML files from markdown posts"""
    posts_dir = Path('posts')
    posts = []
    
    # Process each markdown file
    for md_file in posts_dir.glob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, body = parse_frontmatter(content)
        
        # Skip unpublished posts
        if frontmatter.get('published', 'true').lower() == 'false':
            continue
            
        # Parse date for sorting (supports both date and datetime formats)
        date_str = frontmatter.get('date', '')
        display_date = date_str
        sort_date = date_str
        
        # If date includes time, extract just the date part for display
        if ' ' in date_str:
            display_date = date_str.split(' ')[0]
            sort_date = date_str  # Keep full datetime for sorting
        
        # Convert markdown to HTML
        html_content = markdown_to_html(body)
        
        # Create HTML file
        html_file = posts_dir / f"{md_file.stem}.html"
        
        template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{frontmatter.get('title', md_file.stem)}</title>
    <link rel="icon" type="image/png" href="../favicon.png">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div id="header-placeholder"></div>
    <script>
        // Load header component for blog posts
        async function loadHeader() {{
            try {{
                const response = await fetch('../header.html');
                const headerHTML = await response.text();
                // Update paths for subdirectory
                const updatedHTML = headerHTML
                    .replace(/src="logo\.png"/g, 'src="../logo.png"')
                    .replace(/href="index\.html"/g, 'href="../index.html"')
                    .replace(/href="blog\.html"/g, 'href="../blog.html"')
                    .replace(/href="about\.html"/g, 'href="../about.html"');
                document.getElementById('header-placeholder').outerHTML = updatedHTML;
            }} catch (error) {{
                console.error('Error loading header:', error);
            }}
        }}
        if (document.readyState === 'loading') {{
            document.addEventListener('DOMContentLoaded', loadHeader);
        }} else {{
            loadHeader();
        }}
    </script>
    
    <main>
        <h1>{frontmatter.get('title', md_file.stem)}</h1>
        <p class="post-date">{display_date}</p>
        
        {html_content}
    </main>
</body>
</html>"""
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(template)
        
        # Add to posts list
        posts.append({
            'title': frontmatter.get('title', md_file.stem),
            'date': display_date,  # Date only for display
            'sort_date': sort_date,  # Full datetime for sorting
            'slug': md_file.stem,
            'excerpt': frontmatter.get('excerpt', ''),
            'ai_assisted': frontmatter.get('ai_assisted', 'false').lower() == 'true'
        })
    
    # Sort posts by date (newest first) - use sort_date for proper chronological ordering
    posts.sort(key=lambda x: x['sort_date'], reverse=True)
    
    # Generate blog index
    blog_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog</title>
    <link rel="icon" type="image/png" href="favicon.png">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="header-placeholder"></div>
    <script src="header.js"></script>
    
    <main>
        <h1>All Posts</h1>
        <ul class="post-list">"""
    
    for post in posts:
        ai_tag = '<span class="ai-tag">AI-assisted</span>' if post['ai_assisted'] else ''
        blog_html += f"""
            <li>
                <a href="posts/{post['slug']}.html">
                    <h3>{post['title']} {ai_tag}</h3>
                    <p class="post-date">{post['date']}</p>
                    {f'<p>{post["excerpt"]}</p>' if post['excerpt'] else ''}
                </a>
            </li>"""
    
    blog_html += """
        </ul>
    </main>
</body>
</html>"""
    
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(blog_html)
    
    # Update homepage with recent posts
    recent_posts_html = ""
    for post in posts[:3]:  # Latest 3 posts
        ai_tag = '<span class="ai-tag">AI-assisted</span>' if post['ai_assisted'] else ''
        recent_posts_html += f"""
        <div>
            <a href="posts/{post['slug']}.html">
                <h3>{post['title']} {ai_tag}</h3>
                <p class="post-date">{post['date']}</p>
                {f'<p>{post["excerpt"]}</p>' if post['excerpt'] else ''}
            </a>
        </div>"""
    
    # Read and update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # Replace recent posts section
    updated_content = re.sub(
        r'<div id="recent-posts">.*?</div>',
        f'<div id="recent-posts">{recent_posts_html}</div>',
        index_content,
        flags=re.DOTALL
    )
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)

if __name__ == '__main__':
    generate_blog()
    print("Blog generated successfully!")