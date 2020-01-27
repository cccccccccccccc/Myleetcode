# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:32:46 2018

@author: chen
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getAncestor(self, root, p, q):
        if root.val == p.val or root.val == q.val:
            return root
        if root.val < p.val:
            root = root.right
            return self.getAncestor(root,p,q)
        elif root.val >p.val and root.val < q.val:
            return root
        else:
            root = root.left
            return self.getAncestor(root,p,q)
            
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            tmp = q
            q = p
            p = tmp
        return self.getAncestor(root,p,q)
a = TreeNode(6)
b = TreeNode(2)
c = TreeNode(8)
d = TreeNode(0)
e = TreeNode(4)
f = TreeNode(3)
g = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g
A = Solution()
print(A.lowestCommonAncestor(a,e,e))