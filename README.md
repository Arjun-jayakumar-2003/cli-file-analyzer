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


## Usage

### 1. Clone the repository

git clone https://github.com/Arjun-jayakumar-2003/cli-file-analyzer.git

cd cli-file-analyzer

### 2. Run the program

python3 main.py

### 3. Provide input

- Enter a directory path when prompted  
- Press Enter to analyze the current directory


## Example Output

```
Number of Files: 10

Total Size: 2.35 MB

Largest File By Size: example.txt : 1.20 MB

Number of Files By Extension

.txt -> 5 files
.py -> 3 files
no_extensions -> 2 files
```


## Technologies Used

- Python 3  
- pathlib (for path handling)  
- os (for file and directory operations)  
- collections (for counting and grouping data)  

## Author

**Arjun Jayakumar**  
GitHub: https://github.com/Arjun-jayakumar-2003
