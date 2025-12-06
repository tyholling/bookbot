def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def count_words(text):
    return len(text.split())

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

main()
