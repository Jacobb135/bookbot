def main():
    book_path = "books/frankenstein.txt"
    book = get_book_content(book_path)
    word_count = get_book_word_count(book)
    characters = character_count(book)
    chars_sorted_list = chars_dict_to_sorted_list(characters)
    
    print(f"--- Begin report of {book_path}")
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def get_book_content(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents
    
def get_book_word_count(book):
    words = book.split()
    return len(words)

def character_count(book):
    lowercase_book = book.lower()

    character_counter = {}

    for character in lowercase_book:
        if character in character_counter:
            character_counter[character] = character_counter[character] + 1
        else:
            character_counter[character] = 1

    return character_counter

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for character in num_chars_dict:
        sorted_list.append({"char": character, "num": num_chars_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()