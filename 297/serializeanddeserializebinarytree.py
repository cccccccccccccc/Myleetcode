# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root,string):
            if root == None:
                string += '# '
            else:
                string += str(root.val) + ' '
                string = rserialize(root.left,string)
                string = rserialize(root.right, string)
            return string
        string = rserialize(root, '')
        return string


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            if len(l) == 0:
                return 
            if l[0] == '#':
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root
        data_list = data.split(' ')
        return rdeserialize(data_list)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

