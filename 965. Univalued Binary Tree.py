class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        queue = [root]
        value = root.val

        while queue:
            node = queue.pop(0)
            if value != node.val:
                return False

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

tree = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
solution = Solution()
solution.isUnivalTree(tree)