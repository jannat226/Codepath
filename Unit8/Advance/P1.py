# Problem 1: Ivy Cutting
# You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the 
# rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from 
# the root node to the rightmost leaf node.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you
# believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time
# and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if not root:
        return None
    if not root.right and not root.left:
        return [root.val]
    
    if not root.right:
        root = root.left
        next_path = right_vine(root)
    else:
   
        root = root.right
        next_path = right_vine(root)
        
    return [root.val] + next_path
# Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
# Example Output:

# ['Root', 'Node2', 'Leaf3']
# ['Root']