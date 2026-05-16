# Lab03_6.py
# Group 6 student processing without using imports.
# This program reads student records from a text file and finds students with even IDs.

source_path = "../students.txt"  # Path to the student input file.
destination_path = "group_6.txt"  # Path where the filtered results will be saved.

try:
    with open(source_path, "r") as text_file:  # Open the input file in read mode.
        lines = text_file.readlines()  # Read all lines from the file into a list.
except FileNotFoundError:
    print(f"Error: The input file was not found at {source_path}.")  # Show error when file is missing.
    exit()  # Stop the program when the input cannot be opened.

if len(lines) == 0:
    print("Error: The input file is empty.")  # Notify if the file has no content.
    exit()  # Stop the program because there is nothing to process.  