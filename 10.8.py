def remove_articles(source_file, target_file):
    # Define articles to remove
    articles = {'a', 'an', 'the'}

    try:
        with open(source_file, 'r') as src, open(target_file, 'w') as tgt:
            for line in src:
                # Split line into words and filter out the articles
                words = line.split()
                filtered_words = [word for word in words if word.lower() not in articles]
                
                # Join and write the cleaned line
                tgt.write(' '.join(filtered_words) + '\n')

        print(f"Articles removed and new content written to '{target_file}'")

    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source = 'input.txt'       # Replace with your actual source file
destination = 'output.txt'  # Output file

remove_articles(source, destination)
The quick brown fox jumps over a lazy dog.
An elephant walked through the jungle.
