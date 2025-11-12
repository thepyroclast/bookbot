import sys 
from stats import get_words 
from stats import get_letters_and_count 
from stats import sort_dict 

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    strings = get_book_text(sys.argv[1])
    number_of_words = get_words(strings)
    letter_count = get_letters_and_count(strings)
    sorted_letters = sort_dict(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for dict_pair in sorted_letters:
        print(f"{dict_pair["char"]}: {dict_pair["num"]}")
    #print(sorted_letters)
    print("============= END ===============")
    return

main()    
