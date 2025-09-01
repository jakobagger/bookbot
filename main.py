from stats import count_words, count_chars, sort_chars
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    char_counts = count_chars(book_text)
    sorted_data = sort_chars(char_counts)
    print_report(book_path, num_words, sorted_data)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()