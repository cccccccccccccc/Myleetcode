# Definition for a binary tree node.
"""
construct recusive function use height to be the index of the answer list
when height is the len of List we need to append a [] into the List as its new listlist
append curnode value and recusive traversal its left and right node.

timecomplexity = O(n) spacecomplexity = O(n)
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getlevellist(self,root,height):
        if root is None:
            return
        if height == len(self.levellist):
            self.levellist.append([])
        self.levellist[height].append(root.val)
        self.getlevellist(root.left,height+1)
        self.getlevellist(root.right,height+1)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.levellist = []
        self.getlevellist(root,0)
        return self.levellist

A = Solution()
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e
print(A.levelOrder(a))