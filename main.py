from stats import get_num_words, get_book_text, create_char_dic, sort_dic, get_char_value, get_char_key

def main():
    # print(create_char_dic(get_book_text("./books/frankenstein.txt")))
    # print(sort_dic(create_char_dic(get_book_text("./books/frankenstein.txt"))))
    # get_book_text("./books/frankenstein.txt")
    # print(get_char_key(sort_dic(create_char_dic(get_book_text("./books/frankenstein.txt")))))
    # print(f"{ord("a")}")
    print("============ BOOKBOT ============")  
    print("Analyzing book found at books/frankenstein.txt...") 
    print("----------- Word Count ----------") 
    print(f"Found {get_num_words(get_book_text("./books/frankenstein.txt"))} total words")
    print("--------- Character Count -------")
    for i in get_char_key(sort_dic(create_char_dic(get_book_text("./books/frankenstein.txt"))), "Only Alphabet"):
            print(f"{repr(i)} : {get_char_value(sort_dic(create_char_dic(get_book_text("./books/frankenstein.txt"))), i)}")
    print("============= END ===============")


main()

