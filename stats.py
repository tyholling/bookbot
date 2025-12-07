def count_words(text):
    return len(text.split())

def count_symbols(text):
    text = text.lower()
    counts = {}
    for c in text:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts
