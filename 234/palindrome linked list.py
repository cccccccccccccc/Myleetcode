# Definition for singly-linked list.
"""
timecomplexity = O(n) spacecomplexity = O(1)
get the middle of the list reverse one side of the list 
iterate to check if the two list is the same 

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getlen(self,head):
        count = 0
        while head is not None:
            count +=1
            head = head.next
        return count
    def seperatelist(self,head,listlen):
        mid = listlen//2
        while mid != 0 :
            mid -=1
            head = head.next
        if listlen%2 ==1:
            rightnode = head.next
        else:
            rightnode = head
        return rightnode
    def getrevert(self,node):
        if node is None or node.next is None:
            return node
        head = ListNode(0)
        while node is not None:
            tmpnext = node.next
            node.next = head.next
            head.next = node
            node = tmpnext
        return head.next 
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        listlen = self.getlen(head)
        rightlist = self.seperatelist(head,listlen)
        rightlist = self.getrevert(rightlist)
        while rightlist is not None:
            if head.val != rightlist.val:
                return False
            else:
                head = head.next
                rightlist = rightlist.next
        return True
"""
def isPalindrome(self, head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True
"""
A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(1)
#b.next = c
#a.next = b
print(A.isPalindrome(a))