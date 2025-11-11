def get_words(book_string):
    num_words = 0
    for word in book_string.split():
        num_words += 1
    return num_words

def get_letters_and_count(string):
    lower_string = string.lower()
    characters = {}
    for letter in lower_string:
        if letter in characters:
            characters[letter] = characters[letter] + 1
        else:
            characters[letter] = 1
    return characters



