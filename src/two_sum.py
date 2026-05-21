# PROBLEM: Two Sum
#
# You are given a list of integers `nums` and an integer `target`.
#
# Your task is to find TWO different numbers in the list such that their sum equals the target.
#
# You must return the indices of these two numbers.
#
# Rules:
# - You may NOT use the same element twice.
# - There is exactly one valid solution for each input.
#
# INPUT:
# - nums: List of integers
# - target: Integer
#
# OUTPUT:
# - Return a list containing the two indices [i, j]
#
# EXAMPLE:
# Input:
# nums = [2, 7, 11, 15]
# target = 9
#
# Output:
# [0, 1]
#
# Explanation:
# nums[0] + nums[1] = 2 + 7 = 9

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    # Return empty list if no solution found (though problem guarantees one solution)
    return []


if __name__ == "__main__":
    # Step 1: Get input from user (as text)
    user_input = input("Enter a list of integers (space-separated): ")

    # Step 2: Split the input into separate strings
    string_numbers = user_input.split()

    # Step 3: Convert each string into an integer
    nums = []
    for num in string_numbers:
        nums.append(int(num))

    # Step 4: Get the target number
    target = int(input("Enter the target integer: "))

    # Step 5: Call the function
    result = two_sum(nums, target)

    # Step 6: Print result
    if result:
        print("Indices of the two numbers that add up to", target, ":", result)
    else:
        print("No solution found.")
