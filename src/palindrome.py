def palindrome(word):
    length = len(word) // 2

    for i in range(length):
        if word[i] != word[-(i + 1)]:
            return False
    return True


if __name__ == "__main__":
    word = input("Enter a word: ")

    if palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")
