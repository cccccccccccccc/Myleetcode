"""
timecomplexity = O(n) spacecomplexity = O(1)
iterate single link to get start node m
then think about the question is reverse single link totally
in subfunction
iterate to shift m to right, reverse two adjacent nodes when m == n remember get the original startnode.next to cur node next because after reverse left is to right 
return prev main fuction
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getreverse(self,node,count,n):
        ori = node
        tmp = prev = None
        while node :
            if count != n:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            else:
                ori.next = node.next
                node.next = prev
                prev = node
                break
            count+=1
        return prev
         
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        count = 1
        dew = ListNode(0,head)
        cur = dew
        while cur.next :
            if count == m:
                cur.next = self.getreverse(cur.next,count,n)
                break
            cur = cur.next
            count+=1
        return dew.next
A = Solution()
a = ListNode(100)
b = ListNode(101)
c = ListNode(102)
d = ListNode(103)
e = ListNode(104)
a.next = b
b.next = c
c.next = d
d.next = e
m = 2
n = 2
print(A.reverseBetween(a,m,n))