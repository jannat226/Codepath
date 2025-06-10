# roblem 1: Hunny Hunt
# Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.

def linear_search(lst, target):
    if len(lst) ==0:
        print(-1)
        return
    result = -1
    for i in range(len(lst)):
        
        if lst[i]== target:
            result = i
   
    print(result)
       
# Example Usage:

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)
# Example Output:

# 3
# -1