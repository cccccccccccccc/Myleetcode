# Definition for singly-linked list.
"""
timecomplexity = O(L) L is length of listnode ,spacecomlexity = O(1)
one pass dfs
use recursive remainder length at each level. when find the last node set target node as length-n 
after recursive check if cur level is length-n, if true remove cur.next 
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def _removeNth(self,cur,n,tmplength):
        if cur.next is None:
            self.Nth = tmplength-n
            return  
        self._removeNth(cur.next,n,tmplength+1)
        if tmplength == self.Nth:
            cur.next = cur.next.next
        return
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        newhead = ListNode(0)
        cur = newhead
        cur.next = head
        self.Nth = 0
        if head is None or head.next is None:
            return None
        self._removeNth(cur,n,0)
        return newhead.next
A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
n = 2
print(A.removeNthFromEnd(a,n))