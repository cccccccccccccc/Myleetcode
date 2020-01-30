# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Algorithm

The problem is to calculate the number of unique BST. To do so, we can define two functions:

G(n): the number of unique BST for a sequence of length n.
F(i,n): the number of unique BST, where the number i is served as the root of BST (1≤i≤n).
Later we would see that G(n) can be deducted from F(i,n), which at the end, would recursively refers to G(n).

First of all, following the idea in the section of intuition, we can see that the total number of unique BST G(n), is the sum of BST F(i,n) enumerating each number i (1 <= i <= n) as a root. i.e.

G(n) =∑i=1 n F(i,n)(1)

Particularly, for the bottom cases, there is only one combination to construct a BST out of a sequence of length 1 (only a root) or nothing (empty tree). i.e.

G(0)=1,G(1)=1

Given a sequence 1 ... n, we pick a number i out of the sequence as the root, then the number of unique BST with the specified root defined as F(i, n)F(i,n), 
is the cartesian product of the number of BST for its left and right subtrees, as illustrated below:

For example, F(3, 7), the number of unique BST tree with the number 3 as its root. To construct an unique BST out of the entire sequence [1, 2, 3, 4, 5, 6, 7] with 3 as the root, 
which is to say, we need to construct a subtree out of its left subsequence [1, 2] and another subtree out of the right subsequence [4, 5, 6, 7], 
and then combine them together (i.e. cartesian product). Now the tricky part is that we could consider the number of unique BST out of sequence [1,2] as G(2), 
and the number of of unique BST out of sequence [4, 5, 6, 7] as G(4). For G(n), it does not matter the content of the sequence, but the length of the sequence. 
Therefore, F(3,7) = G(2)⋅G(4). To generalise from the example, we could derive the following formula:

F(i,n)=G(i−1)⋅G(n−i)(2)

By combining the formulas (1), (2), we obtain a recursive formula for G(n)G(n), i.e.

G(n) =∑ i=1 n G(i−1)⋅G(n−i)(3)

According to the algorithm, from 1 to n ,choose i to be the root, and recusive call leftsubtree and rightsubtree.
in each tree , circulation all left and right subtree to construct cur tree
timecomplexity and spacecomplexity see the solution
"""
class Solution:
    def generate_trees(self,start,end):
        if start > end:
            return [None,]
        if (start,end) in self.alltree_map:
            return self.alltree_map[(start,end)]    
        alltree = []
        for i in range(start,end+1):    
            lefttree = self.generate_trees(start,i-1)
            righttree = self.generate_trees(i+1,end)
            for l in lefttree:
                for r in righttree:
                    curroot = TreeNode(i)
                    curroot.left = l
                    curroot.right = r
                    alltree.append(curroot)
        self.alltree_map[(start,end)] = alltree
        return alltree    
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        self.alltree_map = {}
        return self.generate_trees(1,n)if n else []    
            
