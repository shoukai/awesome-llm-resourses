#!/usr/bin/env python3
"""
Markdown processor for awesome-llm-resourses.

This script reads a template markdown file, processes <file> tags,
and converts markdown lists to tables with GitHub badges.
"""

import os
import re
import sys
from pathlib import Path

def extract_github_repo(url):
    """Extract GitHub repository name from URL."""
    if not url or "github.com" not in url:
        return None
    
    # Skip GitHub feature pages, documentation pages, etc.
    if re.search(r'github\.com/features/', url) or \
       re.search(r'github\.com/docs/', url) or \
       re.search(r'github\.com/about/', url):
        return None
    
    match = re.search(r'github\.com/([^/]+/[^/]+)', url)
    if match:
        repo = match.group(1)
        # Remove .git suffix if present
        if repo.endswith('.git'):
            repo = repo[:-4]
        # Check if this is actually a repo path and not a feature path
        if '/' in repo and not any(x in repo for x in ['features', 'docs', 'about']):
            return repo
    return None

def process_list_item(line):
    """Convert a markdown list item to a table row with GitHub badges."""
    # Match pattern: * [Name](URL) - Description
    match = re.match(r'\s*\*\s*\[(.*?)\]\((.*?)\)\s*-\s*(.*)', line)
    if not match:
        return line
    
    name, url, description = match.groups()
    repo = extract_github_repo(url)
    
    if repo:
        github_badge = f"[![GitHub stars](https://img.shields.io/github/stars/{repo}.svg?style=flat-square)](https://github.com/{repo}/stargazers)"
        last_update = f"[![Last commit](https://img.shields.io/github/last-commit/{repo}.svg?style=flat-square)](https://github.com/{repo}/commits)"
    else:
        github_badge = "N/A"
        last_update = "N/A"
    
    return f"| [{name}]({url}) | {description} | {github_badge} | {last_update} |"

def process_markdown_file(file_path):
    """Process a markdown file, converting lists to tables."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return ""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    processed_lines = []
    
    in_list = False
    current_section = None
    
    for i, line in enumerate(lines):
        # Check if this is a heading
        if line.startswith('#'):
            if in_list:
                # End previous table if we were in a list
                processed_lines.append("")
                in_list = False
            processed_lines.append(line)
            current_section = line
        
        # Check if this is a list item
        elif line.strip().startswith('*'):
            if not in_list:
                # Start a new table
                processed_lines.append("")
                processed_lines.append("| 项目 | 详情 | Stars | 最近更新 |")
                processed_lines.append("| :--- | :--- | :---: | :---: |")
                in_list = True
            
            # Convert list item to table row
            processed_lines.append(process_list_item(line))
        
        # Handle empty lines and regular text
        else:
            if in_list and line.strip() == "":
                # Empty line after a list ends the table
                processed_lines.append("")
                in_list = False
            processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def process_template(template_path, output_path):
    """Process the template file and replace <file> tags with processed content."""
    if not os.path.exists(template_path):
        print(f"Template file not found: {template_path}")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Find all <file> tags and store processed content in a dictionary to avoid duplicate processing
    file_tags = re.findall(r'<file>(.*?)</file>', template_content)
    processed_files = {}
    
    # Process each unique file tag
    for file_tag in set(file_tags):
        # Get the absolute path of the referenced file
        if file_tag.startswith('/'):
            # Absolute path within the project
            project_root = Path(template_path).parent
            file_path = project_root / file_tag.lstrip('/')
        else:
            # Relative path
            file_path = Path(template_path).parent / file_tag
        
        print(f"Processing file: {file_path}")
        # Process the referenced file
        processed_content = process_markdown_file(str(file_path))
        processed_files[file_tag] = processed_content
    
    # Replace all file tags with their processed content
    for file_tag, content in processed_files.items():
        template_content = template_content.replace(f'<file>{file_tag}</file>', content)
    
    # Write the processed content to the output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    return True

def main():
    """Main function to process README_template.md and generate README.md."""
    # Get the project root directory
    project_root = Path(__file__).parent.parent
    
    # Define input and output paths
    template_path = project_root / "README_template.md"
    output_path = project_root / "README.md"
    
    print(f"Processing template: {template_path}")
    success = process_template(template_path, output_path)
    
    if success:
        print(f"Successfully generated: {output_path}")
    else:
        print("Failed to process template")
        sys.exit(1)

if __name__ == "__main__":
    main()
