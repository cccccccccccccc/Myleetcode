# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:03:04 2017

@author: chen
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        countone = 0
        if n <=1:
            return n
        tmp = n
        while tmp>1:
            if tmp%2 == 1:
                countone +=1
                tmp-=1
            tmp= int(tmp/2)
            if tmp == 1:
                countone +=1
        return countone

A=Solution()
print(A.hammingWeight())
