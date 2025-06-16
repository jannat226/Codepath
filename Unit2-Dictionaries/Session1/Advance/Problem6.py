# Problem 6: Organize the Pirate Crew

from collections import defaultdict


def organize_pirate_crew(group_sizes):
    '''# Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt.
    Each pirate has a unique ID from 0 to n - 1.

    # You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in.
    # For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.

    # Return a list of groups such that each pirate i is in a group of size group_sizes[i].

    # Each pirate should appear in exactly one group, and every pirate must be in a group. If there are multiple answers, 
    # return any of them. It is guaranteed that there will be at least one valid solution for the given input.
    '''
    result = []
    sizeMap = defaultdict(list)
    for index, value in enumerate(group_sizes):
        sizeMap[value].append(index)
        
        if len(sizeMap[value] )== value:
            result.append(sizeMap[value])
            sizeMap[value] = []
    return result
        
            
            
            
# Example Usage:

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 
# Example Output:

# [[5], [0, 1, 2], [3, 4, 6]]
# [[1], [0, 5], [2, 3, 4]]