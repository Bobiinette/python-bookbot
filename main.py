from stats import get_number_of_words
from stats import get_number_of_each_characters
from stats import sort_character_dictionnary
import sys

def get_book_text(file_path):
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    books = sys.argv[1:]
    # Report starts here
    print("============ BOOKBOT ============")
    for book in books:
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {get_number_of_words(get_book_text(book))} total words")
        print("--------- Character Count -------")
        characters_sorted = sort_character_dictionnary(get_number_of_each_characters(get_book_text(book)))
        for c in characters_sorted:
            print(f"{c['character']}: {c['count']}")
    print("============= END ===============")
    return 0

main()