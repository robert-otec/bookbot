from stats import get_num_words, get_book_text, get_num_characters


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    print(get_num_words(text))
    number_of_characters = get_num_characters(text)
    print(number_of_characters)
    print(text)

main()