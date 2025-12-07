import stats

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = stats.count_words(text)
    print(f"Found {num_words} total words")
    symbols = stats.count_symbols(text)
    print(symbols)

main()
