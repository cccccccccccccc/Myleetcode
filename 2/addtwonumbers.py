class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()     
        node = ListNode((l1.val+l2.val)%10)
        carry = (l1.val+l2.val)//10
        head.next = node
        l1 = l1.next
        l2 = l2.next
        while l1 is not None or l2 is not None:
            val1=val2=0
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            if l2 is not None:
                val2 = l2.val 
                l2 = l2.next          
            node.next = ListNode((val1+val2+carry)%10)
            carry = int((val1+val2+carry)/10)
            node= node.next
        if carry != 0:
            node.next = ListNode(carry)
        return head.next
A = Solution()
a1 = ListNode(9)
a2 = ListNode(9)
a3 = ListNode(3)
a1.next = a2
# a2.next = a3
b1 = ListNode(9)
b2 = ListNode(9)
b3 = ListNode(9)
b1.next = b2
b2.next = b3
print(A.addTwoNumbers(a1,b1))