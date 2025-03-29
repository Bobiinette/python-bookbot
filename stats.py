def get_number_of_words(book_content):
    return len(book_content.split())

def get_number_of_each_characters(book_content):
    book_content = book_content.lower()
    # A dictionnary that will keep track of the count of each character in the book
    characters_count = {}
    for c in book_content:
        if c in characters_count:
            characters_count[c] += 1
        else:
            characters_count[c] = 1
    return characters_count

# return liste of dictionnaries with the format with the format {"character": "a", "count": 10}
def sort_character_dictionnary(character_dictionnary):
    # A list of dictionnaries with the format {"character": "a", "count": 10}
    formated_dictionnary = []
    for c in character_dictionnary:
        duo = {"character": c, "count": character_dictionnary[c]}
        formated_dictionnary.append(duo)
    formated_dictionnary.sort(reverse=True, key=sort_on_count)
    return formated_dictionnary

def sort_on_count(d):
    return d["count"]