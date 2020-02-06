# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
timecomplexity = O(n) spacecomplexity = O(h)
construct recursive function 
check if node's value is in range L to R include L and R
then recursive its children 
when node is equal with L or R do not need to continue check its children 
"""

class Solution:
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sumbst = 0
        def _rangeSumBST(root,L,R):
            if root:
                if L <= root.val<= R:
                    self.sumbst += root.val
                if L < root.val:
                    _rangeSumBST(root.left,L,R)
                if root.val < R:
                    _rangeSumBST(root.right,L,R)
        _rangeSumBST(root,L,R)            
        return self.sumbst
A = Solution()
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(8)
e = TreeNode(20)
a.left = b
a.right = c
b.right = d
c.right = e
L = 7
R = 15
print(A.rangeSumBST(a,L,R))