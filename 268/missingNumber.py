# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:55:56 2018

@author: chen
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = int((0 + len(nums))*(len(nums)+1)/2)
        for i in nums:
            tmp = tmp -i            
        return tmp
a= []
A = Solution()
print(A.missingNumber(a))
        