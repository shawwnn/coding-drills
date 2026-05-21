# PROBLEM: Odd Even Totaler
# INPUT: 10 integers
# TASK:
# - Classify each number as odd or even
# - Compute total sum of odd numbers
# - Compute total sum of even numbers
# OUTPUT:
# - Print odd numbers total
# - Print even numbers total

def odd_even_totaler(numbers):
    odd_total = 0
    even_total = 0

    for num in numbers:
        if num % 2 == 0:
            even_total += num
        else:
            odd_total += num

    return odd_total, even_total


if __name__ == "__main__":
    numbers = []
    for i in range(10):
        num = int(input(f"Enter integer {i + 1}: "))
        numbers.append(num)

    odd_total, even_total = odd_even_totaler(numbers)

    print(f"Total of odd numbers: {odd_total}")
    print(f"Total of even numbers: {even_total}")
