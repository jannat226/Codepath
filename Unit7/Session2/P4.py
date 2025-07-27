# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Write a function next_greatest_letter() that returns the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# Lexicographic order can also be defined as alphabetic order.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def next_greatest_letter(letters, target):
    if not letters:
        return -1
    if ord(letters[0]) - 1  == ord(target):
        return letters[0]
    return next_greatest_letter(letters[1:],target)
        
# Example Usage:

letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

print(next_greatest_letter(letters, 'a'))
print(next_greatest_letter(letters, 'd'))
print(next_greatest_letter(letters, 'y'))
# Example Output:

# b
# Example 1 Explanation: The smallest character lexicographically greater than 'a' in letters is 'b'

# e
# Example 2 Explanation: The smallest character lexicographically greater than 'd' in letters is 'e'

# a
# Example 3 Explanation: There is no character lexicographically greater than 'y' in letters
# so we return letters[0]