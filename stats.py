# Number of words in the string. 
def get_num_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
    
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())


def get_num_character(text):
    char_dict = {}
    
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_num_character(char_dict):
    """
    Sorts the character dictionary by frequency.
    
    Args:
        char_dict (dict): The dictionary containing character counts.
    
    Returns:
        list: A sorted list of tuples (character, count).
    """
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    