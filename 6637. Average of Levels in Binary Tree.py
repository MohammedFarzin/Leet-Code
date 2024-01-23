class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def averageOfLevels(self, root):
        average = [ ]
        queue = [root]
        while queue:
            avg = 0
            length = len(queue)

            for i in range(length):
                node = queue.pop(0)
                avg += node.val
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
            average.append(avg/length)
        return average

tree = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6))
)
solution = Solution()
print(solution.averageOfLevels(tree))

