# task_1.py
# This script reads a file named 'sample.txt' and prints its content line by line.
# It includes error handling for cases where the file is not found.

def read_sample_file():
    """
    Opens and reads 'sample.txt', printing its content with line numbers.
    Handles FileNotFoundError if the file does not exist.
    """
    try:
        # The 'with' statement ensures the file is automatically closed.
        # We open the file in read mode ('r').
        with open('sample.txt', 'r') as file:
            print("Reading file content:")
            # Use enumerate to get both the line number and the line content.
            # Start counting from 1.
            for line_number, line in enumerate(file, 1):
                # .strip() removes leading/trailing whitespace, including the newline character.
                print(f"Line {line_number}: {line.strip()}")
                
    except FileNotFoundError:
        # This block executes if 'sample.txt' isn't found.
        print("Error: The file 'sample.txt' was not found.")

# Main execution block
# This ensures the code inside only runs when the script is executed directly.
if __name__ == "__main__":
    read_sample_file()
