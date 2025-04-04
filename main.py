import sys
from stats import count_character_frequency, sort_dict_to_list
from sys import path
import os

def get_book_text(filepath):
    """
    Reads the contents of a file and returns it as a string.

    Args:
        filepath (str): The path to the file.

    Returns:
        str: The contents of the file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
    

def main():
    """
    Main function to analyze the contents of a book file and print word and character counts.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]  # Use the second argument as the file path
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    book_text = get_book_text(filepath)
    if book_text:  # Only proceed if the file was successfully read
        # Word count
        word_count = len(book_text.split())
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        
        # Character frequency
        char_frequency = count_character_frequency(book_text)
        if char_frequency:
            print("--------- Character Count -------")
            sorted_frequency = sort_dict_to_list(char_frequency)
            for char, freq in sorted_frequency:
                if not char.isalpha():
                    continue
                print(f"{char}: {freq}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()