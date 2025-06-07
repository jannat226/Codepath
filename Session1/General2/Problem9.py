# Problem 9: Odd
# Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.

def get_odds(nums):
    result = []
    for num in nums:
        if num%2 != 0:
            result.append(num)
    print(result)
    
# Example Usage

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)
# Example Output:

# [1, 3]
# []