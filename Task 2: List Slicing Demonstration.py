# task_2.py
# This script demonstrates writing to and appending data to a file based on user input.

def write_and_append_file():
    """
    Takes user input to write to a file, appends more data,
    and then reads and displays the file's final content.
    """
    file_name = 'output.txt'

    # 1. Get user input and write to the file
    try:
        initial_text = input("Enter text to write to the file: ")
        # Open the file in write mode ('w'). This will create the file if it
        # doesn't exist or overwrite it if it does.
        with open(file_name, 'w') as file:
            file.write(initial_text + '\n') # Add a newline for better formatting
        print(f"Data successfully written to {file_name}.")
    except IOError as e:
        print(f"Error writing to file: {e}")
        return # Exit the function if writing fails

    # 2. Get more input and append it
    try:
        additional_text = input("Enter additional text to append: ")
        # Open the file in append mode ('a'). This adds content to the end.
        with open(file_name, 'a') as file:
            file.write(additional_text + '\n')
        print("Data successfully appended.")
    except IOError as e:
        print(f"Error appending to file: {e}")
        return # Exit if appending fails

    # 3. Read and display the final content
    try:
        print(f"\nFinal content of {file_name}:")
        with open(file_name, 'r') as file:
            # Read the entire file content and print it.
            content = file.read()
            print(content.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found for reading.")
    except IOError as e:
        print(f"Error reading file: {e}")


# Main execution block
if __name__ == "__main__":
    write_and_append_file()
