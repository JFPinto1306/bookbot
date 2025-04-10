from stats import get_num_words, get_num_character, sort_num_character
import sys


def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
    
    Returns:
        str: The content of the book file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
  
     
# Main Function
def main():
    """
    Main function to execute the book reading functionality.
    """
    
    print(sys.argv)
    if len(sys.argv) !=  2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    # Get the book text
    book_text = get_book_text(book_path)
    
    num_words = get_num_words(book_text)
    
    # Print the content of the book
    print(f'============ BOOKBOT ============\nAnalyzing book found at {book_path}...')
    print(f'----------- Word Count ----------\nFound {num_words} total words')
    print(f'----------- Character Count -----')
    char_dict = get_num_character(book_text)
    sorted_char_list = sort_num_character(char_dict)
    for char, count in sorted_char_list:
        if char.isalpha():
            print(f'{char}: {count}')    
    print('============= END ===============')
    
    
if __name__ == "__main__":
    main()
    
    
