# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(n)
use a stack to contain all the root's left nodes 
then pop node from stacktree repeatedly add the node.val to answerlist 
check if the node have rightsubtree , add all the leftnode in subtree to the stack
return the answerlist
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pushstack(self, node):        
        while node is not None:
            self.stacktree.append(node)
            node = node.left
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.stacktree = []
        aswlist = []
        self.pushstack(root)        
        while len(self.stacktree)>0:
            node = self.stacktree.pop()
            aswlist.append(node.val)
            self.pushstack(node.right)
        return aswlist

A = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.left = c
print(A.inorderTraversal(a))