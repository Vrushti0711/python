def frequency(text):
    # Convert to lowercase and split into words
    words = text.lower().split()

    # Create dictionary to store frequency
    freq = {}

    for word in words:
        # Strip common punctuation
        word = word.strip(".,!?;:\"()[]{}")
        if word:
            freq[word] = freq.get(word, 0) + 1

    # Return frequency dictionary sorted by word
    return dict(sorted(freq.items()))

# Example usage
input_string = input("Enter a string: ")
word_freq = frequency(input_string)

print("\nWord Frequencies (sorted):")
for word, count in word_freq.items():
    print(f"{word}: {count}")
