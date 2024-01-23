class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:        
    def invert_tree(self, root):
        if not root:
            return root
        print(root.val)

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        root.left, root.right = root.right, root.left
        return root            


tree = TreeNode(2, TreeNode(1), TreeNode(3))
solution = Solution()
solution.invert_tree(tree)

