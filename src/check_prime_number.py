# Check if a number is prime
# Problem:
# Given an integer n, determine if it is a prime number.
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# Example:
# Input:  7
# Output: True
# Input:  10
# Output: False

def check_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    if check_prime_number(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
