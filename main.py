from stats import count_words, charcter_count, sort_stats
import sys

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_contents = get_book_text(path)
    word_count = count_words(book_contents)
    character_stats = charcter_count(book_contents)
    # print(character_stats)
    sorted_character_stats = sort_stats(character_stats)

    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {word_count} total words\n--------- Character Count -------")
    for char in sorted_character_stats:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()
