# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self,s,t):
        if s == None and t == None:
            return True
        if s == None or t== None:
            return False
        if s.val == t.val:
            return self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)
        return False
    def findSubtree(self,s,t):
        if s == None:
            return False  
        return self.isSameTree(s, t) or self.findSubtree(s.left,t) or self.findSubtree(s.right,t)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        result = self.findSubtree(s,t)
        return result