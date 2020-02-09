# Definition for a binary tree node.
"""
timecomplexity = O(n) spacecomplexity = O(n)
BST could be constructed by preorder or postorder travesal only.
That means that BST structure is already encoded in the preorder or postorder traversal and hence they are both suitable for the compact serialization.
Serialization could be easily implemented with both strategies, but for optimal deserialization better to choose the postorder traversal because member/global/static variables are not allowed here.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def gettostring(root):
            #portorder traversal to construct val list
            return gettostring(root.left) + gettostring(root.right) + [root.val] if root else []
        #use map to translate int list to str list and use delimate ' ' tobe string
        return ' '.join(map(str,gettostring(root)))
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(lower = float('-inf'),upper = float('inf')):
        # lower and upper deflaut value  
            if not data or data[-1] < lower or data[-1] > upper:
                #node is null or node isn't belong this subtree return None
                return None
            val = data.pop()
            root = TreeNode(val)
            # change the lower of the right subtree
            root.right = helper(val,upper)
            # change the upper of the left subtree
            root.left = helper(lower,val)
            return root
        # split ' ' from data
        data = [int(x) for x in data.split(' ') if x ]
        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))