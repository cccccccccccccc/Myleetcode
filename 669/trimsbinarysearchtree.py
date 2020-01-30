# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(n)
for every node in the tree node.val may have 3 possibilty with L,R
1 node.val < L then return recusive on node.right
2 node.val > R then return recusive on node.left
3 L < node.val < R  
  continue check node's subtree
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trims(node):
            if not node:
                return None
            if node.val < L:
                return trims(node.right)
            if node.val > R:
                return trims(node.left)
            node.left = trims(node.left)
            node.right = trims(node.right)
            return node
        return trims(root)