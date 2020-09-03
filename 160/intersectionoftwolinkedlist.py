# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == headB:
            return headA
        lengthA = 0
        tmpA = headA
        while tmpA:
            tmpA = tmpA.next
            lengthA +=1
        lengthB = 0
        tmpB = headB
        while tmpB:
            tmpB = tmpB.next
            lengthB +=1
        l = headA
        r = headB
        if lengthA>lengthB:
            m = lengthA-lengthB
            for _ in range(m):
                l = l.next
        elif lengthA<lengthB:
            n = lengthB-lengthA
            for _ in range(n):
                r = r.next
        while l:
            if l != r:
                l = l.next
                r = r.next
            else:
                break
        return l
A = Solution()
a = ListNode(4)
b = ListNode(1)
c = ListNode(5)
d = ListNode(6)
e = ListNode(1)
f = ListNode(8)
g = ListNode(4)
a.next = b
b.next = f
c.next = d
d.next = e
e.next = f
f.next = g
print(A.getIntersectionNode(a,c))      