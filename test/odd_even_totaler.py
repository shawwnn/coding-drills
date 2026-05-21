from src.odd_even_totaler import odd_even_totaler


# --------------------
# UNIT TESTS
# --------------------

assert odd_even_totaler([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (25, 30)
# odds: 1+3+5+7+9 = 25
# evens: 2+4+6+8+10 = 30

assert odd_even_totaler([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == (10, 0)

assert odd_even_totaler([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == (0, 20)

assert odd_even_totaler([]) == (0, 0)

print("All tests passed!")
