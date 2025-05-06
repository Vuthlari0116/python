def modify_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open("week4 / input_file" , 'r') as infile:
            content = infile.readlines()

        # Modify the content (example: convert all text to uppercase)
        modified_content = [line.upper() for line in content]

        # Write the modified content to the output file
        with open('output_file' , 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"File '{input_file}' has been modified and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for file '{input_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user for input and output file names
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    
    modify_file('input_file, output_file')