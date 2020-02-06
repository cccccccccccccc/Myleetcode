# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def _diameterBTree(self,root):
        if not root:
            return 0
        l = self._diameterBTree(root.left)
        r = self._diameterBTree(root.right)
        self.ans = max(self.ans,1+l+r)
        return 1+max(l,r)    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        self._diameterBTree(root)
        return self.ans-1