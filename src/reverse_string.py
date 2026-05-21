# Reverse a String Reverse a given string without built-in reverse functions.

def reverse_string(s):
    # Initialize an empty string to store the reversed result
    reversed_str = ""

    # Iterate through the input string in reverse order
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]

    return reversed_str


if __name__ == "__main__":
    input_string = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(input_string))
