# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def getleftlastnode(self,node):
        if node is None:
            return None
        nextnode = node.right
        tmpleft = self.getleftlastnode(node.left)
        tmpright = self.getleftlastnode(node.right)
        if tmpleft is None and tmpright is None:
            return node        
        if tmpleft is not None:
            node.right = node.left
            node.left = None
            tmpleft.right = nextnode
            if tmpright is not None:
                return tmpright
            else:
                return tmpleft
        else:
            return tmpright
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.getleftlastnode(root)
        return

            

Approach 1:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        right = root.right
        if root.left:
            self.flatten(root.left) # 1->2->3, if not root成立 return, 回到2, 開始執行下面code
            # find the tail of left subtree
            tail = root.left
            while tail.right:
                tail = tail.right
            root.right = root.left
            root.left = None
            tail.right = right
        self.flatten(right)

Approach 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def helper(root):
            if root is None: return None
            helper(root.right)
            helper(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root
        helper(root)