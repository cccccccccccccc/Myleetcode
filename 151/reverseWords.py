# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:39:52 2017

@author: chen
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])
A=Solution()
print(A.reverseWords("this is a beautiful day"))
            
        