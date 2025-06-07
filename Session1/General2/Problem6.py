# Problem 6: Squared
# Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list.

def squared(numbers):
    square = [number * number for number in numbers]
    print(square)
# Example Usage

numbers = [1, 2, 3]
squared(numbers)
# Example Output:

# [1, 4, 9]
