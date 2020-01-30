# Definition for a binary tree node.
"""
timecomplexity = O(n) 

when construct the maximun tree, use a stack to protect the cur element which can be joined to the tree as its sequence
for example 
[3,2,1,6,0,5]
if cur < = stack.pop 
 add next into stack and let cur be pop's rightnode
else pop the element from stack until stack is empty or the element in stack is larger than cur 
put in cur node in stack and let the last one which come out from stack be its leftnode
continue 
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        # construct a list each element is a node
        stack = [TreeNode(nums[0])]        
        for i in nums[1::]:
            node = TreeNode(i)
            # i < stack the last element append node and let it be cur leaf's right
            if i <= stack[-1].val:
                stack[-1].right = node
            else:
                while stack and stack[-1].val < i:
                    #if pop element out make sure it become cur node's leftnode, or the node will be lost
                    node.left = stack.pop()
                # if stack isnot empty after last step, let node be lastnode's rightnode
                if stack:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]

                