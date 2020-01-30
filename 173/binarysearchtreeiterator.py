"""
next()and hasnext() timecomplexity = O(1) spacecomplexity = O(h) h is the heght of the tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        # Stack for the recursion simulation
        self.stack = []
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftsub_inorder(root)
    
    def _leftsub_inorder(self, root):
        # For a given node, add all the elements in the leftsub branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left    

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # Node at the top of the stack is the next smallest element
        topmostsmalnode = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the 
        # helper function for the right child
        if topmostsmalnode.right:
            self._leftsub_inorder(topmostsmalnode.right)
        return topmostsmalnode.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>1


