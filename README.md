# CLI File Analyzer

A command-line tool written in Python that analyzes files in a directory by counting files, calculating total size, identifying the largest file, and grouping files by extension.


## Features

- Counts the total number of files in a directory  
- Calculates the combined size of all files  
- Identifies the largest file by size  
- Groups files based on their extensions  
- Handles invalid paths and permission errors gracefully


## How It Works

The program accepts a directory path from the user and performs the following steps:

- Resolves the given path to an absolute path  
- Validates whether the path exists and is a directory  
- Iterates through all files in the directory (excluding subdirectories)  
- Calculates the size of each file  
- Tracks the largest file  
- Groups files by their extensions  
- Displays the results in a formatted output  
