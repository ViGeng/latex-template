#!/bin/bash

# This script cleans temporary LaTeX files

# Array of file extensions to remove
file_extensions=("log" "aux" "bbl" "blg" "brf" "dvi" "fls" "idx" "ilg" "ind" "lof" "lot" "out" "synctex.gz" "toc" "fdb_latexmk")

# Function to remove files
remove_files() {
    local ext_list="$1"
    find . -type f -name "*.$ext_list" -delete
}

echo "Cleaning temporary LaTeX files..."

# Loop through file extensions and remove files
for ext in "${file_extensions[@]}"; do
    remove_files "$ext"
done

echo "Cleaning temporary LaTeX files complete!"