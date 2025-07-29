# Problem 1: Merging Cookie Orders
# You run a local bakery and are given the roots of two binary trees order1 and order2 where each node in the binary tree 
# represents the number of a certain cookie type the customer has ordered. To maximize efficiency, you want to bake enough of 
# each type of cookie for both orders together.

# Given order1 and order2, merge the order together into one tree and return the root of the merged tree. To merge the orders, 
# imagine that when place one tree on top of the other, some nodes of the two trees are overlapped while others are not.
# If two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the not None node will be used 
# as the node of the new tree.

# Start the merging process from the root of both orders.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution
# has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
from collections import deque
class TreeNode():
    def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def build_tree(values):
    if not values or not values[0]:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        # Left child
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        # Right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root


def print_tree(root):
    if not root:
        print("[]")
        return

    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing Nones for cleaner output
    while result and result[-1] is None:
        result.pop()

    print(result)


def merge_orders(order1, order2):
    if not order1:
        return order2
    if not order2:
        return order1
    # if not order1 and  order2:
    #     return None
   
   # Create new node with sum of both values
    merged = TreeNode(order1.val + order2.val)
    merged.left = merge_orders(order1.left, order2.left)
    merged.right = merge_orders(order1.right, order2.right)
    return merged

# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))
    