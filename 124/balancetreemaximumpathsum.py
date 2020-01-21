# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _maxPSum(self,node):
        if not node:
            return 0
            
        leftmax = max(0,self._maxPSum(node.left))
        rightmax = max(0,self._maxPSum(node.right))
        self.ans = max(self.ans,node.val+leftmax+rightmax)
        return node.val+max(leftmax,rightmax)
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float("-inf")
        self._maxPSum(root)
        return self.ans

A = Solution()
a = TreeNode(-10)
b = TreeNode (20)
c = TreeNode(15)
d = TreeNode(7)
a.left = TreeNode(9)
a.right = b
b.left = c
b.right = d
print(A.maxPathSum(a))