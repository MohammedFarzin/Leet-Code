class TreeNode:
     def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
            node = root
            while node:
                if node.left is None:
                    yield node.val
                    node = node.right
                else:
                    temp = node.left
                    while temp.right and temp.right != node:
                        temp = temp.right
                    
                    if not temp.right:
                        temp.right, node = node, node.left
                    else:
                        yield node.val
                        node, temp.right = node.right, None