# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you
# believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time 
# and space complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_most_specific(root):
    if not root:
        return None
    if root and not root.left and not root.right:
        return [root.val]
    left = get_most_specific(root.left)
    right = get_most_specific(root.right)
    return [left+right]
# Example Usage:

"""
           Plantae
          /       \
         /         \
        /           \ 
Non-flowering     Flowering
   /      \       /        \
Mosses   Ferns Gymnosperms Angiosperms
                             /     \
                        Monocots  Dicots
"""
plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

print(get_most_specific(plant_taxonomy))
# Example Output:

['Mosses', 'Ferns', 'Gymnosperms', 'Monocots', 'Dicots']