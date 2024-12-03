def read_and_modify_file(input_filename, output_filename):
    """
    Reads the content of a file, modifies it, and writes the result to a new file.
    :param input_filename: Name of the file to read (str)
    :param output_filename: Name of the file to write (str)
    """
    try:
        # Read the content of the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Modify the content (Example: Convert to uppercase and add line numbers)
        modified_content = [f"{i+1}: {line.strip().upper()}\n" for i, line in enumerate(content)]
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content successfully written to {output_filename}")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Insufficient permissions to read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main program
try:
    # Ask the user for the input and output filenames
    input_file = input("Enter the name of the file to read: ").strip()
    output_file = input("Enter the name of the file to write the modified content: ").strip()
    
    # Call the function to read and modify the file
    read_and_modify_file(input_file, output_file)
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
