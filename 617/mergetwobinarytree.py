# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(n)
mergeTree is recusive function
create new TreeNode as root and recusivly merge node on t1 t2 to new root
new node.val is t1nodeval plus t2 nodeval
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and  not t2:
            return None
        if not t1 or not t2:
            return t2 or t1
        n = TreeNode(t1.val+t2.val)
        n.left = self.mergeTrees(t1.left,t2.left)
        n.right = self.mergeTrees(t1.right,t2.right)
        return n