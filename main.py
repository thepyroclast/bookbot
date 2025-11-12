def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

from stats import get_words 
from stats import get_letters_and_count 
from stats import sort_dict 
def main():
    strings = get_book_text("./books/frankenstein.txt")
    number_of_words = get_words(strings)
    letter_count = get_letters_and_count(strings)
    sorted_letters = sort_dict(letter_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    print(sorted_letters)
    print("============= END ===============")
    return

main()    
