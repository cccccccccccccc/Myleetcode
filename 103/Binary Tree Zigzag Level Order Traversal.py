"""
timecomplexity = O(n)n is number of node in root. spacecomplexity = O(n) the result list have n nodes .
use dfs
define rlist to remainder all the node in root in zigzag
recursive the tree by depth.
if depth >= len(rlist) means current level is not alive , so append new list in rlist
else have to check index%2 if ==1 and depend on the question level 1 should start from right, so we need to insert each node in this level because node is dfs from left to right
if == 0 we can just add cur node to the end of the rlist[index]
then recursive left tree and right tree index add 1 
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getzigzagLO(self,root, index,rlist):
        if root == None:
            return
        if index>=len(rlist):
            rlist.append([root.val])
        elif index%2 == 1:
            rlist[index].insert(0,root.val)
        else:
            rlist[index]+=[root.val]
        self.getzigzagLO(root.left,index+1,rlist)
        self.getzigzagLO(root.right,index+1,rlist)

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        rlist = []
        self.getzigzagLO(root,0,rlist)
        return rlist

A = Solution()