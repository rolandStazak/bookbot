from stats import get_num_words
from stats import get_num_letters
from stats import sorted_list

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return (file_contents)

def main():
    import sys
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")

    the_book = get_book_text(sys.argv[1])
    word_count = get_num_words(the_book)
    
    print (f"Found {word_count} total words")
    
    print ("--------- Character Count -------")
    
    book_dictionary = {}
    book_dictionary = get_num_letters(the_book)
    
    final_list = sorted_list(book_dictionary)
    
    for item in final_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
    print ("============= END ===============")

main()

