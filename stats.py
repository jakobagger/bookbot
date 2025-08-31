def count_words(text):
    words = text.split()
    return len(words)
    
def count_chars(text):
    word_counts = {}
    for char in text:
        char = char.lower()
        if char in word_counts:
            word_counts[char] += 1
        else:
            word_counts[char] = 1
    
    return word_counts

def sort_on(items):
    return items["num"]

def sort_chars(my_dict):
    char_dicts = []
    for key, value in my_dict.items():
        entry = {"char" : key, "num" : value}
        char_dicts.append(entry)
    char_dicts.sort(reverse=True, key=sort_on)
    return char_dicts