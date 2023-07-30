#!/bin/bash

# This shell removes temporary files in the compiling process.

remove_files() {
    local file_extensions=("$@")
    find . -type f \( "${file_extensions[@]/#/--name *}" \) -delete
}

file_extensions=("log" "synctex.gz" "aux" "fdb_latexmk" "out" "fls" "toc")
remove_files "${file_extensions[@]}"
