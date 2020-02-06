# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(n)
Using a dict to store prefix sum occurs so far 
let sum = from root to cur node val's sum
check how many prefix sums equal to sum - target
then there are same number of subpath that subpathsum = target
remember that when return from subrecusive, need to cancel the curpathsum from dict because the path can only use one childnode
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _getPathSum(self,root,target,curPathSum,dictSum):
        if root is None:
            return
        curPathSum += root.val
        oldPathSum = curPathSum -target
        self.ans += dictSum.get(oldPathSum,0)
        dictSum[curPathSum] = dictSum.get(curPathSum,0) + 1
        self._getPathSum(root.left,target,curPathSum,dictSum)
        self._getPathSum(root.right,target,curPathSum,dictSum)
        dictSum[curPathSum] -= 1
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0
        dictSum = {0:1}
        self._getPathSum(root,sum,0,dictSum)
        return self.ans
#root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
A = Solution()
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(-3)
d = TreeNode(3)
e = TreeNode(2)
f = TreeNode(11)
g = TreeNode(3)
h = TreeNode(-2)
i = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
d.left = g
d.right = h
e.right = i
print(A.pathSum(a,8))