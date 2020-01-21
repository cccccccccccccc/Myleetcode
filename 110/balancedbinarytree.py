# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height (root):
            # help function 
            # find height for the tree
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            return max(l,r) + 1
        
        if not root:
            return True
        h1 = height(root.left)
        h2 = height(root.right)
        # when abs(h1-h2)<=1 need to check if left subtree and right subtree are also be height balance
        if abs(h1-h2) <= 1: 
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

