from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()
