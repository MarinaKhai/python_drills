def m_word_in_square(word: str, size: int):
    """
        The function prints out a square of letters
        which are in fact the 'word' parameter repeated
        as many times as it fits inside the square
    """
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += word[i % len(word)]
        i += 1
    print(row)

if __name__ == "__main__":
    while True:
        word = input("Word: ")
        if word == "":
            break
        size = int(input("Size: "))
        m_word_in_square(word, size)