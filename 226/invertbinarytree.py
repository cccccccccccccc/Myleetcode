# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomlexity = O(1)
inverttree is recusive func
swap root's left and right pointer
then call the recusive function contiue on left and right subtree

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if  not root :
            return root
        root.left ,root.right = root.right, root.left
        if root.left != None:
            self.invertTree(root.left)
        if root.right != None:
            self.invertTree(root.right)
        return root