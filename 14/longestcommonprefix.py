"""
timecomplexity = O(len(strs)*shorteststrlen) spacecomplexity = O(1)
iterate to get minlen in strs 
define i to be the index iterate i which edge is minlen
iterate string in strs, if ansstr'len less than i means no char add into the ansstr so add 
or check if the same index has the same char ,if not return ansstr  until the end 
"""

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        minlen = float("inf")
        for s in strs:
            minlen = min(len(s),minlen)
        i = 0 
        ansstr = ""
        while i < minlen:
            for s in strs:
                if len(ansstr) <= i:
                    ansstr+=s[i]
                elif ansstr[i] != s[i]:
                    return ansstr[:i]
            i+=1
        return ansstr

"""
timecomplexity = O(len(strs)*shorteststrlen) spacecomplexity = O(1)
get the shortest string in strs
iterate the shortest string by enumerate its index and char, iterate the same index with other string in strs
if not equal return shortest string's substring before curindex 
or return the shortest string
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortstr = min(strs,key = len)
        for i, ch in enumerate(shortstr):
            for other in strs:
                if other[i] != ch:
                    return shortstr[:i]   
        return shortstr
A = Solution()
a = ["flower","flow","flight"]
b=[]
c=["a","b","c"]
d=["a"]
print(A.longestCommonPrefix(a))