
def get_book_text(file_contents):
    with open(file_contents) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_string):
    text_split = file_string.split()
    counted_text = len(text_split)
    return counted_text

def create_char_dic(file_string):
    char_ct = {}
    for char in file_string:
        char_low = char.lower()
        if char_low not in char_ct:
            char_ct[char_low] = 0
            char_ct[char_low] += 1
    return char_ct

# def sort_on(items):
#     return 
# 
# def sort_dic(char_dic):
#     char_dic.sort(reverse=True, key)
