def get_book_text(file_path):
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def get_number_of_words(book_content):
    return len(book_content.split())

def main():
    books = ["./books/frankenstein.txt"]
    for book in books:
        print(f"{get_number_of_words(get_book_text(book))} words found in the document")
    return 0

main()