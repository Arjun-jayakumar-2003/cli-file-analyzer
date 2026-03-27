#!/usr/bin/env python3

from pathlib import Path

from collections import defaultdict

import os


def sort_by_extension(file_names):
    print("Number of Files By Extension")
    print("-" * 20)
    print("")
    counts = defaultdict(int)
    for file_name in file_names:
        _, ext = os.path.splitext(file_name)
        if ext == "":
            counts["no_extensions"] += 1
        else:
            counts[ext.lower()] += 1
    counts = sorted(counts.items(), key=lambda x: -x[1])
    for ext, value in counts:
        print(f"{ext} -> {value} files\n")


def formatted_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        else:
            size /= 1024


def file_size_calculator(file_paths, counter):
    largest_file_size = -1
    largest_file_name = ""
    total_size = 0
    for path in file_paths:
        try:
            file_size = os.path.getsize(path)
        except PermissionError:
            continue
        if file_size > largest_file_size:
            largest_file_size = file_size
            _, largest_file_name = path.rsplit("/", 1)
        total_size += file_size
    print(f"Total Size: {formatted_size(total_size)}\n\n")
    if counter > 0:
        print(
            f"Largest File By Size : {largest_file_name} : {formatted_size(largest_file_size)}\n\n"
        )
    else:
        print(f"Largest File By Size : None\n\n")


def file_counter(path):
    counter = 0
    file_paths = []
    if os.path.exists(path) and os.path.isdir(path):
        try:
            items = sorted(os.listdir(path))
        except PermissionError:
            print(f"Permission Denied: {path}\n\n")
            return
        for item in items:
            full_path = os.path.join(path, item)

            if not os.path.isdir(full_path):
                file_paths.append(full_path)
                counter += 1
        print(f"Number of Files: {counter}\n\n")
        file_size_calculator(file_paths, counter)
        sort_by_extension(file_paths)
    else:
        print(f"Invalid Directory : {path}\n\n")


print("CLI File Analyzer\n\n")

user_input = input("Enter path (press Enter for current directory): ").strip()
print()

if not user_input:
    path = os.getcwd()
    path = Path(path).resolve()
else:
    path = Path(user_input).expanduser()
    path = path.resolve()

if not path.exists():
    print(f"Path does not exist: {path}\n\n")
else:
    print(f"Entered Path is {path}\n\n")
    file_counter(path)
