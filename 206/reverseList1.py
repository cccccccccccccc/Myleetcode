# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:23:55 2017

@author: chen
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        tmp1= head
        tmp2 = head.next
        while tmp2 != None:
            tmp3 = tmp2.next
            if tmp1 == head:
                tmp1.next = None
            tmp2.next = tmp1 
            tmp1 =tmp2
            tmp2 = tmp3       
        return tmp1
A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next =b
b.next = c
B = A.reverseList(a)
while B != None:
    print(B.val)
    B = B.next