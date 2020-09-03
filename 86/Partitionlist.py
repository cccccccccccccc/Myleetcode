# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None or head.next is None:
            return head
        lhead = ListNode(0)
        l = lhead
        rhead = ListNode(0)
        r = rhead
        while head:
            tmp = head.next
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = tmp
        r.next = None
        if rhead.next is not None:
            l.next = rhead.next
        return lhead.next
A = Solution()
a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)
a.next =b
b.next = c
c.next = d
d.next = e
e.next = f
print(A.partition(a,3))