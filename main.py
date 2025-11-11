def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

from stats import get_words 
from stats import get_letters_and_count 
def main():
    strings = get_book_text("./books/frankenstein.txt")
    number_of_words = get_words(strings)
    print(f"Found {number_of_words} total words")
    letter_count = get_letters_and_count(strings)
    print(letter_count)
    return

main()    
