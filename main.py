def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

from stats import get_words 

def main():
    string = get_book_text("./books/frankenstein.txt")
    number_of_words = get_words(string)
    print(f"Found {number_of_words} total words")
    return

main()    
