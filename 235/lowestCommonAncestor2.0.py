# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:32:46 2018

@author: chen
"""

# Definition for a binary tree node.
"""
timecomplexity = O(n)
spacecomplexity = O(n)
base on this is a BST , we can make sure let if one node is p and qs' LCA, p<= node's value <=q
so construct recusive function to check 
if node < p 
continue check node.right
if node > q
continue check node.left
if node == p or q 
if p<node<q
node is LCA 
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':       
        def getancentor(node,l, r):
            if not node:
                return None
            if node.val == l or node.val == r:
                return node
            if node.val < l:
                return getancentor(node.right,l,r)
            if node.val > r:
                return getancentor(node.left,l, r)
            if node.val> l and node.val < r:
                return node               
        return getancentor(root, min(p.val,q.val),max(p.val,q.val))
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