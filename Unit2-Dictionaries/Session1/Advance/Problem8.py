
def counting_pirates_action_minutes(logs, k):
    '''
    # The pirate action minutes (PAM) for a given pirate is defined as the number of unique minutes in which the pirate performed
    # an action. A minute can only be counted once, even if multiple actions occur during it.
    # You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k),
    # answer[j] is the number of pirates whose PAM equals j.

# Return the array answer as described above.
'''
# Example Usage:

logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))
# Example Output:

# [0, 2, 0, 0, 0]
# [1, 1, 0, 0]
