from src.palindrome import palindrome


# --------------------
# ASSERT TESTS
# --------------------

assert palindrome("madam") == True
assert palindrome("racecar") == True
assert palindrome("hello") == False
assert palindrome("a") == True
assert palindrome("") == True

print("All tests passed!")
