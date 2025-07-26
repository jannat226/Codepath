# Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's 
# collection, count the total number of unique suits in the list.

def count_suits_iterative(suits):
    hash_map={}
    for suit in suits:
        if suit  in suits:
            hash_map[suit] = 1
        
    result = len(hash_map)
    return result
            

def count_suits_recursive(suits):
    
    if not suits:
        return 0
    if suits[0] in suits[1:]:
        # It's a duplicate, skip it and continue with rest
        return count_suits_recursive(suits[1:])
    else:
        # It's unique, count it and continue with rest
        return 1 + count_suits_recursive(suits[1:])
    
    
print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))