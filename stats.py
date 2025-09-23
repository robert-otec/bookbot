def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_num_characters(text):
    text = text.lower()

    characters = {}

    for char in text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    
    return characters
