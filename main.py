from stats import word_count, get_charactor_count, chars_dict_to_sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(book_path, word_count, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char, count in sorted_characters:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_counts = get_charactor_count(text)
    sorted_characters = chars_dict_to_sorted_list(char_counts)

    print_report(book_path, num_words, sorted_characters)

main()