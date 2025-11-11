def get_words(book_string):
    num_words = 0
    for word in book_string.split():
        num_words += 1
    return num_words