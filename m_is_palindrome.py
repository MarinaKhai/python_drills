""" The function returns True if its argument is a palindrome,
    False otherwise """

def m_is_palindrome(our_str):
    for i in range(len(our_str) // 2):
        if our_str[i] != our_str[len(our_str)-1-i]:
            return False
    return True

def m_is_palindrome_shortest(our_str):
    return our_str == our_str[::-1]


if __name__ == "__main__":
    print("\nType in your string to check, 'enter' to exit")
    while True:
        user_str = input("Your string: ")
        if m_is_palindrome_shortest(user_str):
            print("Yes, this is a palindrome")
        else:
            print("No, this is not a palindrome")

        if user_str == "":
            print("See you soon!")
            break