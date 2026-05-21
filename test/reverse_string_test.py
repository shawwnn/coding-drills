from src.reverse_string import reverse_string


# --------------------
# UNIT TESTS
# --------------------

assert reverse_string("hello") == "olleh"
assert reverse_string("world") == "dlrow"
assert reverse_string("a") == "a"
assert reverse_string("") == ""
assert reverse_string("madam") == "madam"

print("All tests passed!")
