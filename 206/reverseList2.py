# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:02:45 2017

@author: chen
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getlastnode(self, tmp1,tmp2):
        
        if tmp2.next == None:
            tmp2.next = tmp1
            return tmp2 
        tmp3 = self.getlastnode(tmp2,tmp2.next)
        tmp2.next = tmp1
        return tmp3
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head = None or head.next == None:
            return head
        tmp4 = self.getlastnode(head,head.next)
        head.next = None
        return tmp4
        
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
