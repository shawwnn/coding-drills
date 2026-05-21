# PROBLEM: Swap Integer (Without Temporary Variable)

def swap_integer(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


if __name__ == "__main__":
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))

    a, b = swap_integer(a, b)

    print(f"After swapping: a = {a}, b = {b}")
