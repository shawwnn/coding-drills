from src.swap_integer import swap_integer

# --------------------
# ASSERT TESTS
# --------------------

assert swap_integer(3, 5) == (5, 3)
assert swap_integer(10, 20) == (20, 10)
assert swap_integer(-1, 1) == (1, -1)

print("All tests passed!")
