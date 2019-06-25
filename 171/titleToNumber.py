# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:10:10 2018

@author: chen
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        sum = 0
        for index in range(len(s)):
            tmp = s[len(s)-1-index]
            if ord(tmp) < 97:
                tmp1 = 64
            else:
                tmp1 = 96
            letoint = ord(tmp)-tmp1
            sum += letoint*(26**index)
        return sum
    
A = Solution()
print(A.titleToNumber("a"))