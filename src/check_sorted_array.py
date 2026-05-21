# Check if array is sorted

# Problem:
# Given an array of integers, determine if the array is sorted in ascending order.
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: True
# Input:  [3, 1, 4, 2]
# Output: False

def check_sorted_array(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


if __name__ == "__main__":
    # Get input from user
    user_input = input("Enter a list of integers (space-separated): ")

    # Convert input string to list of integers
    numbers = [int(num) for num in user_input.split()]

    # Check if array is sorted
    if check_sorted_array(numbers):
        print("The array is sorted in ascending order.")
    else:
        print("The array is not sorted in ascending order.")
