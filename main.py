from stats import get_num_words, get_book_text, create_char_dic, sort_dic, get_char_value, get_char_key
import sys

def main():
    # print(create_char_dic(get_book_text(sys.argv[1])))
    # print(sort_dic(create_char_dic(get_book_text(sys.argv[1]))))
    # get_book_text(sys.argv[1])
    # print(get_char_key(sort_dic(create_char_dic(get_book_text(sys.argv[1])))))
    # print(f"{ord("z")}")
    # print(sys.argv)
    print("============ BOOKBOT ============")  
    print("Analyzing book found at books/frankenstein.txt...") 
    print("----------- Word Count ----------") 
    print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    for i in get_char_key(sort_dic(create_char_dic(get_book_text(sys.argv[1]))), "Only Alphabet"):
            print(f"{i}: {get_char_value(sort_dic(create_char_dic(get_book_text(sys.argv[1]))), i)}")
    print("============= END ===============")

if len(sys.argv) == 5:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

