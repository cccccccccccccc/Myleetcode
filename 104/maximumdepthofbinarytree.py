"""
timecomplexity = O(n) spacecomplexity = O(n)

func get maxdepth from leftsubtree and rightsubtree recusivly 
get the max from two subtree
remember add 1 for root
compute leftsubtree 
"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l,r)+1

A = Solution()
