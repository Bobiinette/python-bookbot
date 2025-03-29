from stats import get_number_of_words
from stats import get_number_of_each_characters
from stats import sort_character_dictionnary

def get_book_text(file_path):
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    print("============ BOOKBOT ============")
    books = ["./books/frankenstein.txt"]
    for book in books:
        print(f"Analyzing book found at {book[2:]}...")
        print("----------- Word Count ----------")
        print(f"Found {get_number_of_words(get_book_text(book))} total words")
        print("--------- Character Count -------")
        characters_sorted = sort_character_dictionnary(get_number_of_each_characters(get_book_text(book)))
        for c in characters_sorted:
            print(f"{c["character"]}: {c["count"]}")
    print("============= END ===============")
    return 0

main()