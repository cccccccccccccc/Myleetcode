"""
timecomplexity = O(n^2) spacecomplexity = O(1)
iterate the string ,use every char to be the palindromic substring's center word 
construct a helper function to check if left and right side str is same 
remember that there are two kinds of panlindromic substring:
aba
abba
so helper function need to check them both
"""
class Solution:
    def helper (self,s, l ,r):
        while l >=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
        return s[l+1:r]
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ansstr = ""
        for i in range(len(s)-1):
            tmp = self.helper(s,i,i)
            if len(tmp)> len(ansstr):
                ansstr = tmp
            tmp = self.helper(s,i,i+1)
            if len(tmp)> len(ansstr):
                ansstr = tmp           
        return ansstr
from collections import defaultdict
class Solution:
    maxl = 0
    start = 0
    end = 0
    def longestPalindrome(self, s: str) -> str:
        sdict = defaultdict(list)
        for i,v in enumerate(s):
            sdict[v].append(i)
    for k in sdict.keys():
        if len(sdict[k])>=2:
            s