# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        max_depth = 0
        print(f"Visiting node with value: {root.val}")
        for child in root.children:
            child_depth = self.maxDepth(child)
            print(f"Depth of child {child.val}: {child_depth}")
            max_depth = max(max_depth, child_depth)
        print(f"Returning depth for node {root.val}: {max_depth + 1}")
        return max_depth + 1

# Function to initialize values into a Node for an n-ary tree
def initialize_nary_tree(values):
    if not values:
        return None

    root = Node(val=values[0])
    queue = [root]
    index = 1

    while queue and index < len(values):
        current_node = queue.pop(0)

        while index < len(values) and values[index] is not None:
            child = Node(val=values[index])
            current_node.children.append(child)
            queue.append(child)
            index += 1

        index += 1

    return root

# Example usage:
input_values = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
nary_root = initialize_nary_tree(input_values)

# Debugging the maxDepth function
solution = Solution()
max_depth = solution.maxDepth(nary_root)
print("Maximum depth of the n-ary tree:", max_depth)
