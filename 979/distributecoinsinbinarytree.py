# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(n)
root make children balance
balance(root) = val-1+balance(l)+balance(r)
flow(l) = abs(balance(left))
flow(r) = abs(balance(right))
ans +=  flow(l)+flow(r)

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def balance(self,root):
        if root is None:
            return 0
        l = self.balance(root.left)
        r = self.balance(root.right)
        self.ans += abs(l) + abs(r)
        return l + r + root.val-1    
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        self.balance(root)
        return self.ans
A = Solution()
a = TreeNode(1)
b = TreeNode(0)
c = TreeNode(0)
d = TreeNode(3)
a.left = b
a.right = c
b.right = d
print(A.distributeCoins(a))