# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def getlen(self,node):
        count = 0
        while node is not None:
            count+=1
            node = node.next
        return count
    def getsumlist(self,node1,node2,m):
        if node1 is None:
            return None
        cur = ListNode(node1.val)
        if m<=0:
            cur.val += node2.val
            cur.next = self.getsumlist(node1.next,node2.next,m-1)
        else:
            cur.next = self.getsumlist(node1.next,node2,m-1)
        if cur.next is not None and cur.next.val >=10:
            cur.next.val-=10
            cur.val+=1
        return cur
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1 =self.getlen(l1)
        len2 =self.getlen(l2)
        if len1 >= len2:
            tmp1 = l1
            tmp2 = l2
            m = len1-len2
        else:
            tmp1 = l2
            tmp2 = l1
            m = len2-len1
        cur =  self.getsumlist(tmp1,tmp2,m)
        if cur.val >=10:
            head= ListNode(1)
            head.next = cur
            cur.val-=10
            return head
        else:
            return cur
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        prev = None
        while stack1 or stack2 or carry:
            num1 = stack1.pop() if stack1 else 0
            num2 = stack2.pop() if stack2 else 0
            sum_node = num1+num2+carry
            newnode = ListNode(sum_node%10,prev)
            carry = sum_node//10
            prev = newnode
        return prev