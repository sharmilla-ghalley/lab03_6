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
    # Ignore the header row and keep only student data rows.
header_line = lines[0].strip()  # Remove whitespace from the header line.
student_lines = lines[1:]  # All lines after the first are actual student records.

records = []  # Create a list to save parsed student records.
for row in student_lines:
    row = row.strip()  # Remove extra spaces from the current line.
    if row == "":
        continue  # Skip blank lines without data.

    if '\t' in row:
        parts = [item.strip() for item in row.split('\t') if item.strip()]  # Split tab-separated columns.
    elif ',' in row:
        parts = [item.strip() for item in row.split(',') if item.strip()]  # Split comma-separated columns.
    else:
        parts = [item.strip() for item in row.split() if item.strip()]  # Split by whitespace if no tab or comma.

    if len(parts) < 3:
        continue  # Skip rows that do not have three columns.

    records.append((parts[0], parts[1], parts[2]))  # Save serial, name, and ID as a tuple.

if len(records) == 0:
    print("No student records were found after parsing.")  # Notify if parsing found no valid records.
    exit()  # Stop because there is nothing to filter. 

    # Check whether a Student ID ends with an even digit.
def student_id_is_even(student_id):
    student_id = student_id.strip()  # Remove whitespace from the ID.
    if student_id == "":
        return False  # Return False for empty IDs.
    final_digit = student_id[-1]  # Take the last character of the ID.
    return final_digit in ["0", "2", "4", "6", "8"]  # True when the last digit is even.

selected_students = []  # List to store students who belong to Group 6.
for serial, name, student_id in records:
    if student_id_is_even(student_id):  # Check each student ID for evenness.
        selected_students.append((serial, name, student_id))  # Keep the student if the ID is even.

selected_students = sorted(selected_students, key=lambda entry: entry[2])  # Sort the selected records by Student ID.

if len(selected_students) == 0:
    print("No Group 6 students found with even Student IDs.")  # Notify if no student matched the condition.
    exit()  # Stop because the filtered list is empty.