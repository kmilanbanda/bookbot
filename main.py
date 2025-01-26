def word_count(text):
    words = text.split()
    return len(words)

def character_count(string):
    character_dict = {}

    lowercase_string = string.lower()
    for character in lowercase_string:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def print_character_counts(list):
    for entry in list:
        if entry["char"].isalpha():
            print (f"The letter '{entry["char"]}' was found {entry["num"]} times")

def convert_dict_to_dict_list(dict):
    converted_list = []

    for entry in dict:
        new_dict = {}
        new_dict["char"] = entry
        new_dict["num"] = dict[entry]
        converted_list.append(new_dict)

    return converted_list
 
def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents) # prints entire text of designated book

        # prints start of report and word count
        print("Begin report of book(s) ===\n")
        print(f"Final Word Count: {word_count(file_contents)}\n")

        # prepares character count dict-list and sorts it
        dict_list = convert_dict_to_dict_list(character_count(file_contents))
        dict_list.sort(reverse=True, key=sort_on)

        # print character counts and ends report
        print_character_counts(dict_list)
        print("\n=== End Report ===")
main()