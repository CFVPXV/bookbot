from stats import word_count, char_count, sort_char_count
import sys

def get_book_text(filepath):
    bookdata = ""
    with open(filepath) as f:
        bookdata = f.read()
    return bookdata

def print_report(total, word_count, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    for word in word_count:
        if word["char"].isalpha():
            print(f"{word['char']}: {word['num']}")
    print("============= END ===============")

def check_input(input):
    if len(input) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return input[1]


def main():
    innie = sys.argv
    filepath = check_input(innie)
    bookdata = get_book_text(filepath)
    default_data = char_count(bookdata)
    print_report(word_count(bookdata), sort_char_count(default_data), filepath)
main()