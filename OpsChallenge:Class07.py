#!/usr/bin/env python3

import os


def get_directory_info(path):
    """
    This function takes a directory path as input and prints all directories, subdirectories, and files within it.

    Args:
        path: The path to the directory to explore.

    Returns:
        None
    """
    for (root, dirs, files) in os.walk(path):
        print(f"\n== Root Directory: {root} ==")
        print(f"Subdirectories: {', '.join(dirs)}")
        print(f"Files: {', '.join(files)}")


# Get user input for the directory path
user_path = input("Enter the directory path: ")

# Call the function with the user-provided path
get_directory_info(user_path)


