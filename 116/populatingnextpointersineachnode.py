"""
# Definition for a Node.
timecomplexity = O(n) spacecomplexity = O(n)
construct recursive function 
root.left.next is root.right
root.right.next is root.next.left
if root.next is None do not need to do anything
return root
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        if root.left is not None and root.right is not None:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root   
        
A = Solution()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
print(A.connect(a))