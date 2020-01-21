# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _longestUnivaluePath(self,root):
        if not root:
            return 0
        l = self._longestUnivaluePath(root.left)
        r = self._longestUnivaluePath(root.right)
        if not root.left or root.left.val != root.val:
            l = 0
        if not root.right or root.right.val != root.val:
            r = 0
        self.best = max(self.best, l+r+1)
        return 1+max(l,r)
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.best = 0
        self._longestUnivaluePath(root)
        return self.best-1