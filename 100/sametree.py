# Definition for a binary tree node.
"""
timecomplexity = O(n) 
Space complexity : O(log(N)) in the best case of completely balanced tree and )O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.

construct recusive function  check the special tase: two empty tree and one empty one unempty , if the value in two treenode is the same boolen is true and recusivly its two subtree 
return the boolen in the end 
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q:
            return True
        if (not p and q )or(p and not q):
            return False
        if p.val != q.val:
            return False
        is_result = True
        is_result = self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return is_result