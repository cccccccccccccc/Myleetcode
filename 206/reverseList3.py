# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        newhead = ListNode()
        while head is not None:
            remindnext = head.next
            head.next = newhead.next
            newhead.next = head
            head = remindnext
        return newhead.next
    def showans(self,head:ListNode) -> List:
        ans = []
        if head is None:
            return ans
        if head.next is None:
            ans.append(head.val)
        
        while head is not None:
            ans.append(head.val)
            head = head.next
        return ans

A = Solution()
a1 = ListNode(1)
a2 = ListNode(2) 
a3 = ListNode(3) 
a4 = ListNode(4) 
a5 = ListNode(5) 
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
print(A.showans(A.reverseList(a1)))