def main():
    book_path = "github.com/bookbot/books/Frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---")

    num_words = get_num_words(text)
    print(f"{num_words} found in the document")

    chars_dict = get_chars_dict(text)
    print("Character frequencies:")
    for char, count in chars_dict.items():
        print(f"The {char} was found {count} times")
    print ("--End of Report--")
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()