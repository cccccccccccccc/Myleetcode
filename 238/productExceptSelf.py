# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:14:24 2018

@author: chen
"""
# time complexity = O(n) space complexity = O(1)
# use 1 to help 
# newlist = [1,nums,1]
# product all the element on the left side
# product all the element on the right side 
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
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outlist = []
        tmpp = 1
        nlen = len(nums)
        for i in range(nlen):
            outlist.append(tmpp)
            tmpp*=nums[i]
        tmpp = 1
        for i in range((nlen-1),-1,-1):
            outlist[i]*=tmpp
            tmpp*= nums[i]
        return outlist
'''