import stats

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")

    path = "books/frankenstein.txt"
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)
    num_words = stats.count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    symbols = stats.count_symbols(text)
    sorted_symbols = sorted(symbols.items(), reverse=True, key=lambda x: x[1])
    print("--------- Character Count -------")
    for item in sorted_symbols:
        print(f"{item[0]}: {item[1]}")

    print("============= END ===============")

main()
