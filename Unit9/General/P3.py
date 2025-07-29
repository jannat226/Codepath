#  Maximum Tiers in Cake
# You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake, where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different section of your cake, return the maximum number of tiers in your cake.

# The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
from collections import deque
class Puff():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def build_tree(values):
    if not values or not values[0] or len(values) == 0:
        return None

    root = Puff(values[0])
    queue = deque([root])
    index = 1
    
    while queue:
        node = queue.popleft()
         
        if index < len(values) and values[index] is not None:   
            node.left = Puff(values[index])
            queue.append(node.left)
        index += 1
    
        if index < len(values) and values[index] is not None:           
            node.right = Puff(values[index])
            queue.append(node.right)
        index += 1
    return root
        

def print_tree(root):
    if not root:
        return []
    queue = deque(root)
    lst = []
    while queue:
        node = queue.popleft
        if node:
            lst.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    # Remove trailing Nones
    while lst and lst[-1] is None:
        lst.pop()
    return lst
        
        
def max_tiers(cake):
    if not cake : 
        return 0
    queue = deque(cake)
    lst= [cake]
    count = 0
    while queue:
        count +=1
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)                
    return count
        
            
# Example Usage:

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))
