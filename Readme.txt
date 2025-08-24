Python File Handling Assignment
This repository contains the Python scripts for Assignment 4, which focuses on file handling, exceptions, and errors in Python.

Description
This project includes two Python scripts that demonstrate basic file I/O operations: reading from a file with error handling, and writing/appending user-provided data to a file.

Task 1: Read a File and Handle Errors (task_1.py)
This script performs the following actions:

It attempts to open and read a text file named sample.txt.

If the file is found, it reads the content and prints it to the console line by line, prefixed with a line number.

If the file is not found, it catches the FileNotFoundError and prints a user-friendly error message.

Task 2: Write and Append Data to a File (task_2.py)
This script performs the following actions:

Prompts the user to enter some text, which is then written to a file named output.txt.

Prompts the user for additional text, which is appended to the end of output.txt.

Finally, it reads the entire content of output.txt and displays it on the console.

How to Run the Scripts
Clone the repository to your local machine.

Navigate to the project directory in your terminal.

To run Task 1, you can optionally create a sample.txt file in the same directory. Then, execute the script:

python task_1.py

To run Task 2, simply execute the script and follow the on-screen prompts:

python task_2.py
