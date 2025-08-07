
# Write a python program to print the Contents a directory using os modiede. Gearch online for the function which does that.

import os

# Specify the path (you can change this to any directory you want)
path = "/"

try:
    # Get the list of files and directories
    contents = os.listdir(path)

    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"You do not have permission to access '{path}'.")