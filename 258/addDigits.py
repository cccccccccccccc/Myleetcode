# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:04:39 2017

@author: chen
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        tmp = num%9
        if tmp != 0:
            return tmp
        return 9
#        return (num-1)%9+1
#        return num%9 or 9 if num else 0