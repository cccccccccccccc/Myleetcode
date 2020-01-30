# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(n)
consider that :
there are several situation 
1:if root == p or q root is LCA
2: may p and q are in two subtree 
3: may p and q in the same subtree and they are in different level
so construct recusive function 
condition is 
1, root is none return None 
2, root is p or q return root (as consider 1)
3, recusive lefttree and righttree if they both have result return root (as situation 2)
4, if only one subtree is exist return the subtree'result (as situation 3)
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        leftnode = self.lowestCommonAncestor(root.left, p, q)
        rightnode = self.lowestCommonAncestor(root.right, p, q)
        if leftnode != None and rightnode != None:
            return root
        
        return leftnode if not rightnode else rightnode
            