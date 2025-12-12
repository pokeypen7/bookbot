
def get_book_text(file_contents):
    with open(file_contents) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_string):
    text_split = file_string.split()
    counted_text = len(text_split)
    return counted_text

def create_char_dic(file_string):
    char_dic = {}
    for char in file_string:
        char_low = char.lower()
        if char_low not in char_dic:
            char_dic[char_low] = 0
        char_dic[char_low] += 1
    return char_dic


def sort_on(items):
    return items["num"]

def get_char_key(sorted_list, character = None):
    char_key = "char"
    char_list = []
    index = 0
    for index in range(0,len(sorted_list)):
        if character == None:
            char = sorted_list[index][char_key]
            char_list.append(char)
        elif character == "Only Alphabet":
            if ord(sorted_list[index][char_key]) <= 122 and ord(sorted_list[index][char_key]) >= 97 or ord(sorted_list[index][char_key]) >=192 and ord(sorted_list[index][char_key]) <= 383:
                char = sorted_list[index][char_key]
                char_list.append(char)

        elif sorted_list[index][char_key] == character.lower():
            return sorted_list[index][char_key]

    return char_list

def get_char_value(sorted_list, character = None):
    char_key = "char"
    char_value = "num"
    num_list = []
    index = 0
    for index in range(0,len(sorted_list)):
        if character == None:
            num = sorted_list[index][char_value]
            num_list.append(num)
        elif sorted_list[index][char_key] == character.lower():
            return sorted_list[index][char_value]
    return num_list


                





    


def sort_dic(char_dic):
    char_dic_list = []
    char_key = "char"
    char_value = "num"
    for char in char_dic:
        char_dic_sorted = {}
        char_ct = char_dic[char]
        char_dic_sorted[char_key] = char
        char_dic_sorted[char_value] = char_ct
        char_dic_list.append(char_dic_sorted)
    char_dic_list.sort(reverse = True, key = sort_on)
    return char_dic_list