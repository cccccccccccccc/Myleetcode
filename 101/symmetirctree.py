# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(n)
consider all the situation about root and its subtree
construct recusive function pass root.left and right 
check if left == right 
when they both none is true
when their val is equal continue recusive their subtree
else is false
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _isSymmetric(self,left,right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val == right.val:
            return self._isSymmetric(left.left,right.right) and self._isSymmetric(left.right,right.left)
        else:
            return False
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._isSymmetric(root.left,root.right)