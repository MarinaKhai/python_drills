def m_flip_pairs(nmb: int):
    """
        The function returns a list of all the positive integers from 1 up to the number. 
        The numbers' order is changed so that each pair or numbers is flipped.
    """

    i = 1
    sequence_list = []
    while i < nmb:
        sequence_list.extend([i+1, i])
        i += 2
    if nmb % 2 == 1:
        sequence_list.append(i)
    
    return sequence_list

if __name__ == "__main__":
    print("\nEnter a positive integer, a negative or 0 to exit")
    while True:
        try:
            our_nmb = int(input("Number: "))
            if our_nmb < 1:
                break
            print(m_flip_pairs(our_nmb))
        except:
            print("Invalid input")