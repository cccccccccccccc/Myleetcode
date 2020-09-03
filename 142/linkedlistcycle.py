# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow = fast = head
        meet = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = slow
                break
        if meet is None:
            return None
        p1 = head
        p2 = meet
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
A = Solution()
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b

e = ListNode(1)
f = ListNode(2)
e.next = f
f.next = e
print(A.detectCycle(e))