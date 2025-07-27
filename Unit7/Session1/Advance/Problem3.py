# Problem 3: Counting Unique Suits
# Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of unique suits in the list.

# Implement the solution iteratively.
# Implement the solution recursively.
# Discuss: what are the similarities between the two solutions? What are the differences?
# Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
from collections import defaultdict
def count_suits_iterative(suits):
    count = 0
    if count == 0:
        hashMap = defaultdict()
    for suit in suits:
        if suit in hashMap:
            pass
        else:
            hashMap[suit] += 1
            
        return len(hashMap)
            
def helper(hashMap, suit):
    if suit not in hashMap:
        hashMap[suit] +=1
    return 
def count_suits_recursive(suits):
    hashMap={}
    return helper(hashMap,suits)
    


print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))



# 3
# 2