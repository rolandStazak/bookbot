def get_num_words(book_text):
    words_list = book_text.split()
    num_words = len(words_list)
    return (num_words)

def get_num_letters(book_text):
    letter_dictionary = {}
    for char in book_text:
        char = char.lower()
        if (char in letter_dictionary):
            letter_dictionary[char] += 1
        else:
            letter_dictionary[char] = 1
    return letter_dictionary

def sorted_list(book_dictionary):
    sorted_dictionary =[]
    for item in book_dictionary:
        new_dict = {"char": item,"num": book_dictionary[item]}
        sorted_dictionary.append(new_dict)

    def sort_on(items):
        return items["num"]
    
    sorted_dictionary.sort(reverse=True, key=sort_on)
      
    return (sorted_dictionary)

    
