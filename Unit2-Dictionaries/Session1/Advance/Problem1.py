# Problem 1: Counting Treasure
#
def total_treasure(treasure_map):
    ''' Captain Blackbeard has a treasure map with several clues that point to different locations on an island.
    Each clue is associated with a specific location and the number of treasures buried there. 
    Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures
    buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.
    '''
    count = 0 
    for key,value in treasure_map.items():
        count += value
    return count
        
    
# Example Usage:

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasure(treasure_map1)) 
print(total_treasure(treasure_map2)) 
# Example Output:

# 15
# 50