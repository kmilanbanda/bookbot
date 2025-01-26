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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(f"Final Word Count: {word_count(file_contents)}")
        print(f"Final Character Count: {character_count(file_contents)}")
        # print
main()