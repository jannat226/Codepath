# Problem 7: Minimum Number of Steps to Match Treasure Maps
# Captain Blackbeard has two treasure maps represented by two strings of the same length map1 and map2. In one step, you can choose any character of map2 and replace it with another character.

# Return the minimum number of steps to make map2 an anagram of map1.

def min_steps_to_match_maps(map1, map2):
    freq = {}
    for char in map1:
        freq[char]= freq.get(char,0)+1
    for char in map2:
        if char in freq:
            freq[char] -= 1
        else:
            freq[char] = -1
    steps = 0
    for val in freq.values():
        if val > 0:
            steps += val  # map2 needs more of this char
    return steps
        
# Example Usage:

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
# Example Output:

# 1
# 6
# 0