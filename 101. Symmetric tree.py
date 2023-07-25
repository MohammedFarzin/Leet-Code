class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode):
        if not root:
            return root
        
        return self.is_same(root.left, root.right)
    
    def is_same(self, left_root, right_root):
        if left_root is None and right_root is None:
            return True
        if left_root is None or right_root is None:
            return False
        
        if left_root.val != right_root.val:
            return False
        
        return self.is_same(left_root.left, right_root.right) and self.is_same(left_root.right, right_root.left)
    
