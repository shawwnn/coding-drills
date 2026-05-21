from src.fibonacci import fibonacci

# --------------------
# ASSERT TESTS
# --------------------

assert fibonacci(0) == []
assert fibonacci(1) == [0]
assert fibonacci(5) == [0, 1, 1, 2, 3]
assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

print("All tests passed!")
