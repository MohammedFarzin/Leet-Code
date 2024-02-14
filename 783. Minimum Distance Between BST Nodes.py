# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    pre = -float('inf')
    res = float('inf')
    def minDiffInBST(self, root) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res

tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
sl = Solution()

sl.minDiffInBST(tree)