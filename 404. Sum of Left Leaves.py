# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, False)])
        ans = 0

        while queue:
            node, is_left = queue.popleft()

            if not node.left and not node.right and is_left:
                ans += node.val
            
            if node.left:
                queue.append((node.left, True))
            
            if node.right:
                queue.append((node.right, False))
        return ans2