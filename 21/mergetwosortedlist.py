# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:       
            return l2
        if l2 is None:
            return l1
        head = ListNode()
        if l1.val <= l2.val:
            node = l1
            l1 = l1.next
        else:
            node = l2
            l2 = l2.next
        head.next =node
        while l1 is not None or l2 is not None:
            if l1 is None:
                node.next = l2
                break
            if l2 is None:
                node.next = l1
                break
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node=node.next
        return head.next
A = Solution()
a1 = ListNode(1)
a2 = ListNode(2)             
a3 = ListNode(4)
a1.next = a2
a2.next = a3
b1 = ListNode(1)
b2 = ListNode(3)             
b3 = ListNode(4)
b1.next = b2
b2.next = b3
print(A.mergeTwoLists(a1,b1))