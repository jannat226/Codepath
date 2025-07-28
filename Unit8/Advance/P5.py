class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if not root:
        return 0
    if isinstance(root.val, int):
        return root.val
    left = calculate_yield(root.left)
    right = calculate_yield(root.right)
    if root.val == '-':
        return left - right
    elif root.val == '+':
        return left + right
    elif root.val == '*':
        return left * right
    elif root.val == '/':
        return left / right  # Optional for division
    else:
        raise ValueError(f"Unknown operator: {root.val}")
    


# """
#       +
#      / \ 
#     /   \
#    -     *
#   / \   / \
#  4   2 10  2
# """

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))
# print(get_decision(apple_tree))
# Example Output:

# 22
# Explanation:
# - 4 - 2 = 2
# - 10 * 2 = 20
# - 2 + 20 = 22