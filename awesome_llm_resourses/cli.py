#!/usr/bin/env python3
"""
Command-line interface for awesome-llm-resourses markdown processor.

Usage:
    python -m awesome_llm_resourses.cli [--template TEMPLATE] [--output OUTPUT]
"""

import argparse
import os
import sys
from pathlib import Path

from awesome_llm_resourses.md_processor import process_template


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Process markdown templates with file tags and convert lists to tables."
    )
    parser.add_argument(
        "--template",
        "-t",
        help="Path to the template file (default: README_template.md)",
        default="README_template.md",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Path to the output file (default: README.md)",
        default="README.md",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    # Get the project root directory
    project_root = Path(__file__).parent.parent
    
    # Resolve template and output paths
    template_path = Path(args.template)
    if not template_path.is_absolute():
        template_path = project_root / template_path
    
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = project_root / output_path
    
    if args.verbose:
        print(f"Project root: {project_root}")
        print(f"Template path: {template_path}")
        print(f"Output path: {output_path}")
    
    print(f"Processing template: {template_path}")
    success = process_template(template_path, output_path)
    
    if success:
        print(f"Successfully generated: {output_path}")
        return 0
    else:
        print("Failed to process template")
        return 1


if __name__ == "__main__":
    sys.exit(main())
