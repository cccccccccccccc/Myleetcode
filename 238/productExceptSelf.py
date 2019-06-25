# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:14:24 2018

@author: chen
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(n):
            output.append(p)
            p = p*nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i]*p
            p = p*nums[i]
        return output
A = Solution()
print(A.productExceptSelf([3,2,1]))