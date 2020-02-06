# Definition for a binary tree node.

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.levellist = []
        level = 0
        def _levelOrderBottom(root,level):
            if root:
                if level == len(self.levellist):
                    self.levellist.insert(0,[])
                self.levellist[-(self.level+1)].append(root.val)
                _levelOrderBottom(root.left,level+1)
                _levelOrderBottom(root.right,level+1)
        _levelOrderBottom(root,level)
        return self.levellist
A = Solution()
a = TreeNode(3)
b = TreeNode(8)
c = TreeNode(20)
d = TreeNode(1)
e = TreeNode(35)
a.left = b
a.right = c
b.left = d
c.right = e
print(A.levelOrderBottom(a))