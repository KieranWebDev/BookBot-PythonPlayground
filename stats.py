def word_count(book_text):
    return len(book_text.split())

def get_charactor_count(book_text):
    letter_dictionary: dict[str, int] = {}

    book_text = book_text.lower()

    for letter in book_text:
        if letter not in letter_dictionary:
            letter_dictionary[letter] = 1
        else :
            letter_dictionary[letter] += 1

    return letter_dictionary

def sort_on(letter: tuple[str, int]) -> int:
    return letter[1]


def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list = []

    for char in char_dict:
        count = char_dict[char]
        sorted_list.append((char, count))

    return sorted(sorted_list, key=sort_on, reverse=True)