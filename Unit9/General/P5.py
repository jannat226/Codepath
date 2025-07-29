# At your bakery, you organize your current stock of baked goods in a binary tree with root inventory where each node represents the quantity of a baked good in your bakery. A customer comes in wanting a random assortment of baked goods of quantity order_size. Given the root inventory and integer order_size, return True if you can fulfill the order and False otherwise. You can fulfill the order if the tree has a root-to-leaf path such that adding up all the values along the path equals order_size.

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
    queue = deque([root])
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
def can_fulfill_order(inventory, order_size):
    if not inventory:
        return False
    
    # Subtract current node's value from target
    remaining = order_size - inventory.val
    
    # If we're at a leaf, check if remaining is 0
    if not inventory.left and not inventory.right:
        return remaining == 0
    
    # Recursively check left and right subtrees
    left = inventory.left and can_fulfill_order(inventory.left, remaining)
    right = inventory.right and can_fulfill_order(inventory.right, remaining)
    
    return left or right
    
# Example Usage:

"""
             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   
"""

# Using build_tree() function included at top of the page
quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))