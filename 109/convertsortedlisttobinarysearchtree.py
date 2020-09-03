# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getBST(self,head,end):
        print(f'{head.val if head is not None else None}  {end.val if end is not None else None}')
        if head == end:
            return
        middle = right = head
        while right != end and right.next != end:
            middle = middle.next
            right = right.next.next
        root = TreeNode(middle.val)
        print(root.val)
        root.left = self.getBST(head,middle)
        root.right = self.getBST(middle.next,end)
        return root
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.getBST(head,None)
A = Solution()
a = ListNode(-10)
b = ListNode(-3)
c = ListNode(0)
d = ListNode(5)
e = ListNode(9)
a.next = b
b.next = c
c.next = d
d.next = e
print(A.sortedListToBST(a))