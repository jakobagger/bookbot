from stats import count_words, count_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    char_counts = count_chars(book_text)
    sorted_data = sort_chars(char_counts)
    print("""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------""")
    
    print(f"{num_words} words found in the document.")
    print("--------- Character Count -------")
    for item in sorted_data:
        if (item["char"].isalpha()):
            print(item["char"],":", item["num"])

main()