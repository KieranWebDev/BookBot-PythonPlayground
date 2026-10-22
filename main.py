from stats import word_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

text = get_book_text("books/frankenstein.txt")
num_words_in_book = word_count(text)
print(f"Found {num_words_in_book} total words")