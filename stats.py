def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    words = text.lower()
    character_count = {}
    for ch in words:
        if ch in character_count:
            character_count[ch] += 1
        else:
            character_count[ch] = 1
    return character_count

def sort_characters(character_count):
    character_list = []
    for ch, num in character_count.items():
        if ch.isalpha() == True:
            character_list.append({"char": ch, "num": num})
        else:
            continue
    def key_on_num(item):
        return item["num"]
    character_list.sort(key=key_on_num, reverse=True)
    return character_list