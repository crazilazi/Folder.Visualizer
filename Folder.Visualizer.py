#!/usr/bin/env python3
"""
Project Structure Visualizer
----------------------------
A tool to visualize the folder structure of any project directory.
Can be used to visualize .NET, Angular, React, C# or any other project structure.
"""

import os
import argparse
import sys
from pathlib import Path
import re

class ProjectStructureVisualizer:
    def __init__(self, root_dir=None, output_file=None, ignore_patterns=None, 
                 max_depth=None, show_files=True, include_hidden=False):
        self.root_dir = os.path.abspath(root_dir) if root_dir else os.getcwd()
        self.output_file = output_file
        self.ignore_patterns = ignore_patterns or []
        self.max_depth = max_depth
        self.show_files = show_files
        self.include_hidden = include_hidden
        
        # Compile ignore patterns
        self.ignore_regex = [re.compile(pattern) for pattern in self.ignore_patterns]
        
        # Common directories to ignore by default
        self.default_ignores = [
            re.compile(r'node_modules'),
            re.compile(r'\.git'),
            re.compile(r'\.vs'),
            re.compile(r'__pycache__'),
            re.compile(r'bin'),
            re.compile(r'obj'),
            re.compile(r'dist'),
            re.compile(r'build'),
            re.compile(r'\.vscode'),
            re.compile(r'\.idea')
        ]
    
    def should_ignore(self, path):
        """Check if a path should be ignored based on patterns."""
        name = os.path.basename(path)
        
        # Skip hidden files/folders if not explicitly included
        if not self.include_hidden and name.startswith('.'):
            return True
            
        # Check against default ignore patterns
        for pattern in self.default_ignores:
            if pattern.search(path):
                return True
                
        # Check against user-provided ignore patterns
        for pattern in self.ignore_regex:
            if pattern.search(path):
                return True
                
        return False
    
    def generate_tree(self, start_path=None, current_depth=0):
        """Generate a tree representation of the directory structure."""
        if start_path is None:
            start_path = self.root_dir
            
        if self.max_depth is not None and current_depth > self.max_depth:
            return []
            
        if self.should_ignore(start_path):
            return []
            
        result = []
        
        # Get all directories and files in the current path
        try:
            items = sorted(os.listdir(start_path))
        except PermissionError:
            result.append(f"[Permission Denied]")
            return result
            
        dirs = []
        files = []
        
        for item in items:
            full_path = os.path.join(start_path, item)
            if os.path.isdir(full_path):
                if not self.should_ignore(full_path):
                    dirs.append(item)
            elif self.show_files and not self.should_ignore(full_path):
                files.append(item)
        
        # Process directories first
        for i, d in enumerate(dirs):
            is_last_dir = (i == len(dirs) - 1 and len(files) == 0)
            full_path = os.path.join(start_path, d)
            
            if is_last_dir:
                result.append(f"└── {d}/")
                subtree = self.generate_tree(full_path, current_depth + 1)
                for line in subtree:
                    result.append(f"    {line}")
            else:
                result.append(f"├── {d}/")
                subtree = self.generate_tree(full_path, current_depth + 1)
                for line in subtree:
                    result.append(f"│   {line}")
        
        # Then process files
        for i, f in enumerate(files):
            if i == len(files) - 1:  # Last item
                result.append(f"└── {f}")
            else:
                result.append(f"├── {f}")
                
        return result
    
    def visualize(self):
        """Generate and display the directory structure."""
        tree = self.generate_tree()
        
        # Add the root directory to the beginning
        root_name = os.path.basename(self.root_dir)
        if not root_name:  # In case of root directory
            root_name = self.root_dir
            
        output = [f"{root_name}/"]
        for line in tree:
            output.append(line)
            
        # Output the result
        if self.output_file:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(output))
            print(f"Structure written to {self.output_file}")
        else:
            print('\n'.join(output))
            
        return output


def main():
    parser = argparse.ArgumentParser(description='Visualize project folder structure')
    parser.add_argument('-d', '--directory', help='Root directory to visualize (default: current directory)')
    parser.add_argument('-o', '--output', help='Output file (default: print to console)')
    parser.add_argument('-i', '--ignore', action='append', help='Patterns to ignore (can be used multiple times)')
    parser.add_argument('-m', '--max-depth', type=int, help='Maximum depth to traverse')
    parser.add_argument('-n', '--no-files', action='store_true', help='Do not show files, only directories')
    parser.add_argument('--include-hidden', action='store_true', help='Include hidden files and directories')
    
    args = parser.parse_args()
    
    visualizer = ProjectStructureVisualizer(
        root_dir=args.directory,
        output_file=args.output,
        ignore_patterns=args.ignore,
        max_depth=args.max_depth,
        show_files=not args.no_files,
        include_hidden=args.include_hidden
    )
    
    visualizer.visualize()


if __name__ == "__main__":
    main()
