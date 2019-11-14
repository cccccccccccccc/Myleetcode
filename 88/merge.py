# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:24:05 2018

@author: chen
"""
"""
time complexity = O(n) space complexity = 0
can think about this from the last index m+n-1 judge m-1 n-1 which one is bigger  
remeber if m <=0 need to insert nums2 into nums1

"""
from typing import List
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:  
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1