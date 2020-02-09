# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(n)
Here is the algorithm:

Construct inorder traversal of the tree. It should be an almost sorted list where only two elements are swapped.

Identify two swapped elements x and y in an almost sorted array in linear time.

Change value x to y and value y to x.
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inordertree(root:TreeNode)->List[TreeNode]:
            return inordertree(root.left) + [root] + inordertree(root.right) if root else []
        
        def findswapnode(inorderlist:List[TreeNode]) -> None:
            n = len(inorderlist)-1
            node1 = node2 = None
            for i in range(n):
                if inorderlist[i+1].val < inorderlist[i].val:
                    node2 = inorderlist[i+1]
                    if node1 is None:
                        node1 = inorderlist[i]
                    else:
                        break
            node1.val,node2.val = node2.val,node1.val
        nodelist = inordertree(root)
        findswapnode(nodelist)
