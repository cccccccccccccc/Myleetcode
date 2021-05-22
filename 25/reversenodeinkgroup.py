"""
timecomplexity = O(n) spacecomplexity = O(1)
iterate to get the length of linked list, Divide by k, so we know how many sublinked list to be reverse
iterate each sub list
input prevnode  remind old head  iterate to reverse each node  after that linked newhead to prevnode and linked old head'next to next node 
return old head as next iterate's input
"""
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
            tmp = node.next # first remind next 
            node.next = prev #swap
            prev = node # shift 
            node = tmp
        prev0.next = prev # prevtail'next is new head
        remind.next = node # old head's next is next node
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
            cur = self.getreversebyK(cur,k)  # return is next sublinked list prevtail
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