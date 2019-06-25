# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getsize(self,head):
        
        cur = 0
        if head == None:
            return cur
        p = head
        while p!= None:
            p = p.next
            cur+=1
        return cur
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        sizeA = self.getsize(headA)
        sizeB = self.getsize(headB)
        if sizeA == 0 or sizeB == 0:
            return None
        if sizeA >=sizeB:
            tmp1 = headA
            tmp2 = headB
            maxlink = sizeA
            dif = sizeA-sizeB
        else:
            tmp1 = headB
            tmp2 = headA
            maxlink = sizeB
            dif = sizeB-sizeA
        i = 1
        while i <= maxlink:
            if i <= dif:
                tmp1= tmp1.next
            else:
                if tmp1 != tmp2:
                    tmp1 = tmp1.next
                    tmp2 = tmp2.next
                else:
                    return tmp1
            i+=1
        return None
        
a = ListNode(3)
b = ListNode(2)
b.next = a
A = Solution()
print (A.getIntersectionNode(a,b))