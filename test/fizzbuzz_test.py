from src.fizzbuzz import fizzbuzz

# --------------------
# ASSERT TESTS
# --------------------

assert fizzbuzz(1) == [1]

assert fizzbuzz(3) == [1, 2, "Fizz"]

assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]

assert fizzbuzz(15)[-1] == "FizzBuzz"

print("All tests passed!")
