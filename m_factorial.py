def iterative_factorial(nmb: int):
    i = j = 1
    while j <= nmb:
        i *= j
        j += 1

    return i

if __name__ == "__main__":
    print("\nEnter a positive integer, a negative or 0 to exit")
    while True:
        try:
            our_nmb = int(input("Number: "))
            if our_nmb < 1:
                break
            print("Iterative factorial:", iterative_factorial(our_nmb))
        except:
            print("Invalid input")