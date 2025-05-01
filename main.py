from stats import get_num_words, count_chars, char_report
import sys

def get_book_text(filepath: str):
    with open(filepath) as f:
        contents = f.read()

    return contents

def print_char_report(report: list[dict]):
    for line in report:
        if line["char"].isalpha():
            print(f"{line["char"]}: {line["num"]}")

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = args[1]
    text = get_book_text(filepath)
    count = get_num_words(text)
    char_counts = count_chars(text)
    report = char_report(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    print_char_report(report)

if __name__ == '__main__':
    main()
