def get_number_of_words(book_content):
    return len(book_content.split())

def get_number_of_each_caracters(book_content):
    book_content = book_content.lower()
    # A dictionnary that will keep track of the count of each caracter in the book
    caracters_count = {}
    for c in book_content:
        if c in caracters_count:
            caracters_count[c] += 1
        else:
            caracters_count[c] = 1
    return caracters_count