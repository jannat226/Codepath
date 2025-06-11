# Problem 4: Sort Array by Parity
# Given an integer array nums, write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

def sort_by_parity(nums):
    even = [x for x in nums if x % 2 == 0]
    odd = [x for x in nums if x % 2 != 0]
    print(even + odd) 
                   
# Example Usage

nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)
# Example Output:

# [2, 4, 3, 1]
# [0]