# Definition for a binary tree node.
"""
construct recusive function use height to be the index of the answer list
when height is the len of List we need to append a [] into the List as its new listlist
append curnode value and recusive traversal its left and right node.

timecomplexity = O(n) spacecomplexity = O(n)

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

"""
from collections import deque
from typing import List
class TreeNode:x
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None
class Solution:
    def levelOrder(self,root: TreeNode) -> List[List[int]]:
        if root is None:
            return[]
        nodedeque = deque()
        aswlist = []
        nodedeque.append([root,0])
        while len(nodedeque) != 0:
            tmplist = nodedeque.popleft()
            tmpnode = tmplist[0]
            tmpheigh = tmplist[1]
            if tmpheigh == len(aswlist):
                aswlist.append([])
            aswlist[tmpheigh].append(tmpnode.val)
            if tmpnode.left is not None:
                nodedeque.append([tmpnode.left, tmpheigh+1])
            if tmpnode.right is not None:
                nodedeque.append([tmpnode.right,tmpheigh+1])
        return aswlist
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

