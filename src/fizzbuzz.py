# PROBLEM: FizzBuzz
# INPUT: Integer n
# OUTPUT: List from 1 to n with rules:
# - Multiples of 3 → "Fizz"
# - Multiples of 5 → "Buzz"
# - Multiples of 3 and 5 → "FizzBuzz"
# - Otherwise → number

def fizzbuzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(fizzbuzz(n))
