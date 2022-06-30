def m_are_anagrams(str1, str2):
    """ The function returns True if str1 and str2 are anagrams
        in relation to each other, False otherwise"""
    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    print(m_are_anagrams("tame", "mate"))
    print(m_are_anagrams("tame", "team"))
    print(m_are_anagrams("python", "java"))