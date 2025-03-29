from stats import get_number_of_words
from stats import get_number_of_each_characters

def get_book_text(file_path):
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    books = ["./books/frankenstein.txt"]
    for book in books:
        print(f"{get_number_of_words(get_book_text(book))} words found in the document")
        print(get_number_of_each_characters(get_book_text(book)))
    return 0

main()