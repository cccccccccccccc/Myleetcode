# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countgoodnode(self, node, maxgood):
        if node is None :
            return
        if maxgood <= node.val:
            self.num+=1
            maxgood = node.val
        self.countgoodnode(node.left,maxgood)
        self.countgoodnode(node.right,maxgood)

    def goodNodes(self, root: TreeNode) -> int:
        self.num = 0
        maxgood = -10**5
        self.countgoodnode(root,maxgood)
        return self.num