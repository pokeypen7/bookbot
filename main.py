from stats import get_num_words, get_book_text, create_char_dic

def main():
    print(f"Found {get_num_words(get_book_text("./books/frankenstein.txt"))} total words")
    print(create_char_dic(get_book_text("./books/frankenstein.txt")))
    # get_book_text("./books/frankenstein.txt")


main()

