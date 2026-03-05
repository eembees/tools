#!/usr/bin/env python3
# /// script
# dependencies = ["pyyaml"]
# ///
"""
Scan all HTML tool files and generate _data/tools.yml for the index page.
Reads <title> and <meta name="description"> from each file.
"""
import os
import re
import yaml

EXCLUDE = {'index.html', '404.html'}

def extract_meta(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read(4096)  # only need the <head>

    title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else None

    desc_match = re.search(
        r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']',
        content, re.IGNORECASE
    ) or re.search(
        r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']',
        content, re.IGNORECASE
    )
    description = desc_match.group(1).strip() if desc_match else None

    return title, description

def main():
    tools = []
    for filename in sorted(os.listdir('.')):
        if not filename.endswith('.html') or filename in EXCLUDE:
            continue
        title, description = extract_meta(filename)
        entry = {
            'file': filename,
            'url': '/' + filename,
            'title': title or filename.replace('.html', '').replace('-', ' ').replace('_', ' ').title(),
        }
        if description:
            entry['description'] = description
        tools.append(entry)

    os.makedirs('_data', exist_ok=True)
    with open('_data/tools.yml', 'w', encoding='utf-8') as f:
        yaml.dump(tools, f, allow_unicode=True, default_flow_style=False)

    print(f"Generated _data/tools.yml with {len(tools)} tool(s)")

if __name__ == '__main__':
    main()
