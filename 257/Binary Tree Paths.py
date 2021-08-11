# Definition for a binary tree node.
"""
timecomplexity = O(n)
remember the question is find all root to leaf path so important thing is to find leaf
leafnode no left and right
use recursive to get path 
"""
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getTreePaths(self,node,treepath):
        if node:
            treepath+=str(node.val)
            if not node.left and not node.right:
                self.ans.append(treepath)
                return
            treepath+="->"
            self.getTreePaths(node.left,treepath)
            self.getTreePaths(node.right,treepath)
        return
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []
        self.getTreePaths(root,"")
        return self.ans