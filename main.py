from stats import get_num_words
from stats import get_character_count
from stats import sort_characters

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    sorted_chars = sort_characters(character_count)
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
'Found {num_words} total words'
--------- Character Count -------""")
    for item in sorted_chars:
        print(f"'{item['char']}: {item['num']}'")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()
