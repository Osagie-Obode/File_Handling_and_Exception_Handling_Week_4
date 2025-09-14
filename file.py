# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as infile:
        data = infile.read()

    # Modify the content (e.g., convert to uppercase)
    data_new = data.upper()

    with open('output.txt', 'w') as outfile:
        outfile.write(data_new)                 #write to a new file

    print("File has been modified and saved as output.txt.")

except FileNotFoundError:
    print(f"{filename} not found.")  # Handles the case where the input file does not exist

except PermissionError:
    print(f"Permission denied: cannot read {filename}.")  # Handles permission errors

except Exception as e:
    print(f"An error occurred: {e}")  # Catches any other exceptions and prints the error
