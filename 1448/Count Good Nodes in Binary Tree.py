"""
timecomplexity = O(N) n number of tree node.
dfs recursive to check each node value and maxval if >= change maxvalue and add count 
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def getgoodNodes(self, node,maxvalue):
        if node is None:
            return 
        if node.val >= maxvalue:
            self.count+=1
            maxvalue = node.val
        self.getgoodNodes(node.left,maxvalue)
        self.getgoodNodes(node.right,maxvalue)
        return
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        maxvalue = root.val
        self.getgoodNodes(root,maxvalue)
        return self.count
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