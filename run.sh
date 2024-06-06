#!/bin/bash

# Directory containing the Python files
DIR="crons"

# Find and execute each Python file
for file in "$DIR"/*.py
do
  python "$file"
done

DIR="eng"

# Find and execute each Python file
for file in "$DIR"/*.py
do
  python "$file"
done
