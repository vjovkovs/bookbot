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
    

def count_words(text):
    """
    Counts the number of words in a given string.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    return len(text.split())


def get_num_words(filepath):
    """
    Counts the number of words in a book file.

    Args:
        filepath (str): The path to the book file.

    Returns:
        int: The number of words in the book.
    """
    book_text = get_book_text(filepath)
    return count_words(book_text)
    
def count_character_frequency(text):
    """
    Counts the frequency of each character in the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary where keys are characters (lowercased) and values are their frequencies.
    """
    frequency = {}
    for char in text.lower():  # Convert all characters to lowercase
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def sort_dict_to_list(dictionary):
    """
    Sorts a dictionary by its values in descending order and returns a list of tuples.

    Args:
        dictionary (dict): The dictionary to sort.

    Returns:
        list: A list of tuples sorted by the dictionary's values in descending order.
    """
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
