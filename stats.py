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