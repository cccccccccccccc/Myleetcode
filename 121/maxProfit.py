# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:43:57 2017

@author: chen


class Solution(object):
    def maxProfit(self, prices):
        
        #:type prices: List[int]
        #:rtype: int
        if len(prices) <=1:
            return 0
        minp = prices[0]
        maxp = 0
        best = 0
        for i in prices[1:]:
            if i <= minp:
                minp = i
                maxp=0
            else:                
                if i >maxp:
                    maxp = i
                    if maxp-minp>best:
                        best = maxp-minp
        return best
A= Solution()
print(A.maxProfit([3,2,6,5,0,3]))

"""
'''
time complexity=O(n) space complexity = O(1) 
best = max{best,a[i]-x}
x = min{x, a[i]}

'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        if len(prices)<=1:
            return best
        buy = prices[0]        
        for i in prices[1:]:
            if buy >= i:
                buy = i
            else:
                best = max(best, (i-buy))

        return best
    

A = Solution()
a = [7,6,5,3,1]
print(A.maxProfit(a))