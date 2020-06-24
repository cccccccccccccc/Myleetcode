# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getmerge(self,l1,l2):
        head = ListNode(0)
        tail = head
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                l1,l2 = l2,l1
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        if l1 is None :
            tail.next = l2
        if l2 is None:
            tail.next = l1
        return head.next
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slownode = head
        fastnode = head.next
        while fastnode is not None and fastnode.next is not None:
            slownode = slownode.next
            fastnode = fastnode.next.next  
        mid = slownode.next
        slownode.next = None
        return self.getmerge(self.sortList(head),self.sortList(mid))
A = Solution()
a1 = ListNode(4)
a2 = ListNode(2)
a3 = ListNode(1)
a4 = ListNode(3)
a1.next = a2
a2.next = a3
a3.next = a4
print(A.sortList(a1))