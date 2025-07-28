class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
res = []
def survey_tree(root):
    if not root:
        return None

    survey_tree(root.left)
    survey_tree(root.right)
    res.append(root.val)
    return res
    
#     pass
# Example Usage:

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))
['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root']