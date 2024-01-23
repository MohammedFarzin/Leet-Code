class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1


        if root1 is None:
            return root2


        root1.val += root2.val 
        print(root1.val)
        root1.left = self.mergeTrees(root1.left, root2.left)
        
        root1.right = self.mergeTrees(root1.right, root2.right)

tree1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
tree2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))

# Create an instance of Solution
solution = Solution()

# Call mergeTrees method by passing the root nodes
merged_tree = solution.mergeTrees(tree1, tree2)