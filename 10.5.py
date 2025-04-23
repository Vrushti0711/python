def copy_and_convert_to_upper(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        
        # Convert content to uppercase
        upper_content = content.upper()
        
        with open(destination_file, 'w') as dest:
            dest.write(upper_content)
        
        print(f"Content copied from '{source_file}' to '{destination_file}' with lowercase converted to uppercase.")
    
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source = 'input.txt'      # Replace with the path to your source file
destination = 'output.txt'  # Replace with the path to your destination file

copy_and_convert_to_upper(source, destination)
