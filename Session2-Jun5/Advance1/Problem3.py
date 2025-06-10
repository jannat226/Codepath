# Problem 3: Remove Duplicates
# Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.

def remove_dupes(items):
    hashMap = {}
    count = 0 
    for item in items:
        if item not in hashMap:
            hashMap[item]= 1
            count+=1
        else:
            items.remove(item)
    print(count)
    
        
# Example Usage

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)
# Example Output:

# 4
# 4