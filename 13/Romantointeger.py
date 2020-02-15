"""
timecomplexity = O(n) spacecomplexity = O(1)
use dictonry to contain key and value
iterate string when dict[s[i]] < dict[s[i+1]] means it is 4 or 9 now so we can sub cur value and add next value 
so do as below remain the edge index do not out of range and make sure string is not empty
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        if s == "":
            return 0
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        for i in range(len(s)-1):
            if roman[s[i]]<roman[s[i+1]]:
                sum -= roman[s[i]]
            else:
                sum += roman[s[i]]
        return sum + roman[s[-1]]