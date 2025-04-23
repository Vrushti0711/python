def merge_alternate_lines(file1, file2, output_file):
    try:
        # Open all files
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
            # Read all lines from both files
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            
            # Get the max length of both files
            max_len = max(len(lines1), len(lines2))
            
            # Merge alternately
            for i in range(max_len):
                if i < len(lines1):
                    out.write(lines1[i])
                if i < len(lines2):
                    out.write(lines2[i])
                    
        print(f"Lines merged alternately from '{file1}' and '{file2}' into '{output_file}'.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

# Example usage:
file1 = 'file1.txt'         # Replace with your first input file
file2 = 'file2.txt'         # Replace with your second input file
output = 'merged_output.txt'  # File to write the merged output

merge_alternate_lines(file1, file2, output)
