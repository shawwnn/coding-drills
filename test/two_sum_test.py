from src.two_sum import two_sum


# --------------------
# UNIT TESTS
# --------------------

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
# 2 + 7 = 9

assert two_sum([3, 2, 4], 6) == [1, 2]
# 2 + 4 = 6

assert two_sum([3, 3], 6) == [0, 1]
# 3 + 3 = 6

assert two_sum([1, 5, 8, 10], 9) == [0, 2]
# 1 + 8 = 9

print("All tests passed!")
