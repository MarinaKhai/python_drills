def m_flip_ends(nmb: int):
    """
        The function returns a list of all the positive integers from 1 up to the number. 
        The numbers order in the list is altering between the two ends of the range.
        E.g our number is 7, then the list will be: 1, 7, 2, 6, 3, 5, 4
    """

    i = 1
    sequence_list = []
    while i < nmb / 2:
        sequence_list.extend([i, nmb-i+1])
        i += 1
    sequence_list.append(i)
    if nmb % 2 == 0:
        sequence_list.append(nmb-i+1)
    
    return sequence_list

if __name__ == "__main__":
    print("Enter a positive integer or 0 to exit")
    while True:
        our_nmb = int(input("Number: "))
        if our_nmb == 0:
            break
        print(m_flip_ends(our_nmb))