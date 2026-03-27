# CLI File Analyzer

A simple command-line tool written in Python that analyzes files in a directory.

## Features

- Counts total number of files
- Calculates total size of all files
- Identifies the largest file
- Groups files by extension

## How It Works

The program takes a directory path as input and:
- Lists all files in the directory
- Calculates their sizes
- Categorizes them based on extensions

## Usage

Run the script:

python3 main.py

Then enter a path when prompted.

Press Enter to analyze the current directory.

## Example Output

Number of Files: 10

Total Size: 2.35 MB

Largest File By Size: example.txt : 1.20 MB

Number of Files By Extension

.txt -> 5 files  
.py -> 3 files  
no_extensions -> 2 files

## Technologies Used

- Python
- pathlib
- os
- collections

## Author

Arjun Jayakumar
