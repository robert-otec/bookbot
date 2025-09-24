def get_num_words(text):
    num_words = text.split()
    return len(num_words)
    

def get_chars_dict(text):
    text = text.lower()

    characters = {}

    for char in text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []

    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list