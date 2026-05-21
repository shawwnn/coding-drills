# ---------------------------------------------------
# PROBLEM: Fibonacci Series (First N Terms)
# ---------------------------------------------------
# The Fibonacci sequence is a series where each number
# is the sum of the two previous numbers.
#
# It starts with:
# 0, 1, 1, 2, 3, 5, 8, ...
#
# Your task is to generate the first n terms of this sequence.
#
# ---------------------------------------------------
# INPUT:
# - An integer n representing number of terms
#
# ---------------------------------------------------
# OUTPUT:
# - Print the first n Fibonacci numbers in one line
#
# ---------------------------------------------------
# EXAMPLE:
# Input:
# 7
#
# Output:
# 0 1 1 2 3 5 8
# ---------------------------------------------------

def fibonacci(n):
    result = []

    a = 0
    b = 1

    for _ in range(n):
        result.append(a)

        c = a + b
        a = b
        b = c

    return result


if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print(*fibonacci(n))
