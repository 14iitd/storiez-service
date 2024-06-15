#!/bin/bash

# Directory containing the Python files
DIR="rss"

# Find and execute each Python file
for file in "$DIR"/*.py
do
  python3 "$file"
done
