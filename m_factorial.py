def iterative_factorial(nmb: int):
    i = j = 1
    while j <= nmb:
        i *= j
        j += 1

    return i

if __name__ == "__main__":
    while True:
        our_nmb = int(input("Number: "))
        
        if our_nmb < 1:
            break
        print("Iterative factorial:", iterative_factorial(our_nmb))