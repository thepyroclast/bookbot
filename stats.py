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

def sort_dict(characters_dict):
    new_list = []
    for key in characters_dict.keys():
        if key.isalpha():
            new_list.append({"char": key, "num": characters_dict[key]})
        else:
            continue
    
    def get_num(a):
        return a["num"]
    
    new_list.sort(key=get_num, reverse=True)
    return new_list
