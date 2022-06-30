def m_chessboard_pattern(size: int):
    """
        The function prints out a square of 0s and 1s
        which are arranged in the chessboard-like
        manner. The size of square is 'size'
    """
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10" * size
        else:
            row = "01" * size
        i += 1
        print(row[0:size])


if __name__ == "__main__":
    while True:
        size = int(input("Size: "))
        if size == 0:
            break
        m_chessboard_pattern(size)