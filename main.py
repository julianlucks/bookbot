def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_frequency = count_character_frequency(text)
    
    # Generate and print the report
    print_report(book_path, num_words, char_frequency)


def get_book_text(path):
    """Read the contents of the book from a file."""
    with open(path) as f:
        return f.read()


def get_num_words(text):
    """Count the number of words in the text."""
    words = text.split()
    return len(words)


def count_character_frequency(text):
    """
    Count the frequency of each character in the text.
    Convert text to lowercase and ignore non-alphabetic characters.
    """
    text = text.lower()  # Convert to lowercase
    frequency = {}
    
    for char in text:
        if char.isalpha():  # Only consider alphabetic characters
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    
    return frequency


def print_report(book_path, num_words, char_frequency):
    """Print a nicely formatted report of word and character data."""
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    # Sort characters by frequency (highest to lowest) for a cleaner report
    sorted_characters = sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


if __name__ == "__main__":
    main()
