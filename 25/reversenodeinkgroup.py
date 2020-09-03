# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getreversebyK(self, prev,k): 
        remind = prev.next
        node = prev.next
        prev0 = prev
        for _ in range(k):
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        prev0.next = prev
        remind.next = node
        return remind
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or head is None or head.next is None:
            return head
        #get the lengh of the list
        length = 0
        test = head
        while test:
            length+=1
            test = test.next
        count = length // k
        if count == 0:
            return head
        dew = ListNode(0)
        cur = dew
        cur.next = head
        for _ in range(count):
            cur = self.getreversebyK(cur,k)
        return dew.next
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
k = 2
print(A.reverseKGroup(a,k))    