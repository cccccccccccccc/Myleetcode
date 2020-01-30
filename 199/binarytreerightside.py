# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(h)
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getrightSidefirstnode(self,node,height):
        if not node :
            return 
        if height > len(self.aswlist):
            self.aswlist.append(node.val)
        self.getrightSidefirstnode(node.right,height+1)
        self.getrightSidefirstnode(node.left,height+1)
        return

    def rightSideView(self, root: TreeNode) -> List[int]:
        self.aswlist = []
        self.getrightSidefirstnode(root,1)
        return self.aswlist