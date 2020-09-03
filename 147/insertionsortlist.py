# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionList(self,dew,node):
        cur = dew
        isinsert = False
        while cur.next:
            if cur.next.val <= node.val:
                cur = cur.next
                continue
            else:
                node.next = cur.next
                cur.next = node
                isinsert = True
                break
        if isinsert != True:
            cur.next = node
        return
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = ListNode(head.val,None)
        dew = ListNode(0,cur) 
        head = head.next
        while head:
            tmp = head.next
            head.next = None
            self.insertionList(dew,head)
            head = tmp
        return dew.next

A = Solution()
a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)
a.next = b
b.next = c
c.next = d
print(A.insertionSortList(a))