# Definition for a binary tree node.
"""
timecomplexity = O(logn*logn) spacecomplexity = O(n)
count the most leftside and rightside leaf's height from root 
check 
if their height is equal means the tree is full with all nodes return 2^height -1
else recusion the root's leftsubtree and rightsubtree and count their node
return leftsubtree node + rightsubtreenode + 1(root)
hints: at least one side's subtree is completion 2^height-1  

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getLeftSideHeight(self, root):
        if not root:
            return 0
        return self.getLeftSideHeight(root.left)+1
    def getRightSideHeight(self, root):
        if not root:
            return 0
        return self.getRightSideHeight(root.right)+1       
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftheight = self.getLeftSideHeight(root.left)+1
        rightheight = self.getRightSideHeight(root.right)+1
        if leftheight == rightheight:
            return 2**leftheight-1
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
            