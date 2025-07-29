# Problem 2: Croquembouche
# You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), 
# for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and want to
# send it to the couple for review.

# Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche
# , that prints a list of the flavors (vals) of each cream puff in level order (i.e., from left to right, level by level).

# Note: The build_tree() and print_tree() functions both use variations of a level order traversal.
# To get the most out of this problem, we recommend that you reference these functions as little as possible
# while implementing your solution.

# Evaluate the time complexity of your function. Define your variables and provide a rationale
# for why you believe your solution has the stated time complexity. Assume the input tree is balanced
# when calculating time complexity.
from collections import deque
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right



def build_tree(values):
    if not values or not values[0]:
        return None

    root = Puff(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        # Left child
        if index < len(values) and values[index] is not None:
            node.left = Puff(values[index])
            queue.append(node.left)
        index += 1

        # Right child
        if index < len(values) and values[index] is not None:
            node.right = Puff(values[index])
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

def print_design(design):
    if not design:
        return 
   
    result = []
    queue = deque([design])
    
    while queue:
        node = queue.popleft()
        if node : 
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return result


"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print(print_design(croquembouche))
# Example Output:

# ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']