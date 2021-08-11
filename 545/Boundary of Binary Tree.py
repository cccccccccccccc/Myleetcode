# Definition for a binary tree node.
"""
timecomplexity = O(n) 
separate to iterate tree by leftboundary rightboundary ,check if node belong to left or right boundary  if left is not none node = node.left elif right is not none node
= node.right. if both none mean the node is leaf break 
recrustive to find leave in tree 
remember to reverse rightboundary 
at least sub all these list together
"""
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getleaf(self,node,leafbd):
        if node.left is None and node.right is None:
            leafbd.append(node.val)
        if node.left :
            self.getleaf(node.left,leafbd)
        if node.right:
            self.getleaf(node.right,leafbd)
        
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        leftbd = []
        rightbd = []
        leafbd =[]
        node = root.left
        while node is not None:
            tmp = node.val
            if node.left is not None:
                node = node.left
            elif node.right is not None:
                node = node.right
            else:
                break
            leftbd.append(tmp)
        node = root.right
        while node is not None:
            tmp = node.val
            if node.right is not None:
                node = node.right
            elif node.left is not None:
                node = node.left
            else:
                break
            rightbd.append(tmp)
        self.getleaf(root,leafbd)
        rightbd.reverse()
        return [root.val] + leftbd + leafbd+ rightbd
A = Solution()
root = TreeNode(1)
