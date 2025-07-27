# Problem 3: Find First and Last Frequency Positions
# The Rebel Alliance has intercepted a crucial sequence of encrypted transmissions from the evil Empire. 
# Each transmission is marked with a unique frequency code, represented as integers, and these codes are stored 
# in a sorted array transmissions. As a skilled codebreaker for the Rebellion, write a function find_frequency_positions() 
# that returns a tuple with the first and last indices of a specific frequency code target_code in transmissions.
# If target_code does not exist in transmissions, return (-1, -1).

def find_frequency_positions(transmissions, target_code):
    if len(transmissions) == 0:
        return 
    pass
# Example Usage:

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))
# Example Output:

# (3, 4)
# (-1, -1)
# (-1, -1)