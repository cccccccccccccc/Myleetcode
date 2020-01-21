# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Implement helper function helper(left, right), which constructs BST from nums elements between indexes left and right:

If left > right, then there is no elements available for that subtree. Return None.

Pick left middle element: p = (left + right) // 2.

Initiate the root: root = TreeNode(nums[p]).

Compute recursively left and right subtrees: root.left = helper(left, p - 1), root.right = helper(p + 1, right).

Return helper(0, len(nums) - 1).
"""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left,right):
            if left > right:
                return None
            p = (left + right)//2
            root = TreeNode(nums[p])

            root.left = helper(left,p-1)
            root.right = helper(p+1,right)
            return root

        return helper(0,len(nums)-1)