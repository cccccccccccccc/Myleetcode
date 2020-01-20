# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftsub_inorder(root)
    
    def _leftsub_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left    

    def next(self) -> int:
        """
        @return the next smallest number
        """
        topmostsmalnode = self.stack.pop()

        if topmostsmalnode.right:
            self._leftsub_inorder(topmostsmalnode.right)
        return topmostsmalnode.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>1


