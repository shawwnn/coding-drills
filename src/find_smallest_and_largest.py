# Problem:
# Given an array of integers, find the smallest and largest number in the array.

# Example:
# Input:  [5, 2, 9, 1, 7]
# Output: Smallest = 1, Largest = 9

# Constraints:
# - The array will have at least one element
# - You are not allowed to use built-in min() or max() functions (for practice)

def find_smallest_and_largest(arr):
    if not arr:
        return None, None  # Handle empty array case

    smallest = arr[0]
    largest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest


if __name__ == "__main__":
    # Get input from user
    user_input = input("Enter a list of integers (space-separated): ")

    # Convert input string to list of integers
    numbers = [int(num) for num in user_input.split()]

    # Find smallest and largest
    smallest, largest = find_smallest_and_largest(numbers)

    # Print results
    print(f"Smallest: {smallest}, Largest: {largest}")
