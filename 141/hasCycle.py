# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:34:17 2017

@author: chen
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        middleN = endN = head
        count = 1
        while endN != None:
            if endN.next ==None:
                return False
            endN = endN.next            
            if count%2 ==0:
                middleN = middleN.next
            if endN == middleN:
                return True
            count+=1
        return False
    
a= ListNode(0)
b = ListNode(1)
c = ListNode(2)
a.next = b
b.next = c
c.next  = b
D = None
A = Solution()
print(A.hasCycle(D))