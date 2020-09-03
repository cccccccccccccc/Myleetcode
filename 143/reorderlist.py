# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        start = head
        end = head
        while end and end.next:
            start = start.next
            end = end.next.next
        stack = []
        while start:
            stack.append(start)
            start=start.next        
        cur = head
        while stack :
            tail = stack.pop()
            if cur != tail:
                cur.next,tail.next,cur = tail,cur.next,cur.next
        cur.next = None
        return head
A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
print(A.reorderList(a))
            