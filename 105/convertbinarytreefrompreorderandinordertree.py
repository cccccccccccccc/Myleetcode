"""
time complexity = O(n) space complexity = O(n)
define a map which val:index is enumerate from inorder list 
use recusive function helper(left,right) to construct tree
use preorder list to get everylevel's rootnode point pre_idx from [0]
use the map to find left and right subtrees' range 
and recusivly leftsubtree and rightsubtree to the end 
"""
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def helper(left,right):
            # if there is no elements to construct subtrees
            if left == right:
                return None
            nonlocal pre_idx
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            inx = idx_map[root_val]
            pre_idx +=1
            
            root.left = helper(left,inx)
            root.right = helper(inx+1,right)
            return root
        pre_idx = 0
        idx_map = {val:inx for inx,val in enumerate(inorder)}
        return helper(0,len(preorder))

A = Solution()
a = [3,9,20,15,7]
b = [9,3,15,20,7]
print(A.buildTree(a,b))
