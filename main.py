import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    chars_list = []
    for char, count in num_chars.items():
        char_dict = {"char": char, "num": count}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for item in chars_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()