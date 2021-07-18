"""
timecomplexity = O(n*w^2) spacecomplexity = O(n*w) 
n is number of words w is length of word[i]
dp[j] 1-j if the word can be break
dp[i]= dp[x]and worddict[x+1-1:j] x is between 1 to j
similar with leetcode 139
"""
from collections import defaultdict
from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        worddict = defaultdict(int)
        cword = []
        for i,w in enumerate(words):
            worddict[w]=i
        
        for i,w in enumerate(words):
            if w == "":
                continue
            dp = [False]*(len(w)+1)
            dp[0] = True
            for j in range(1,len(w)+1):
                for x in range(0,j):
                    if dp[x]:
                        rightword = w[x+1-1:j] # dp is padding from 0 - len(w) and dp[0] = true, so when we map dp index to word index we need to reduce by 1
                        if rightword in worddict.keys() and i != worddict[rightword]:
                            dp[j] = True
                            break
            if dp[len(w)]:
                cword.append(w)

        return cword
A = Solution()
a = ["ab","cd","abcd"]
print(A.findAllConcatenatedWordsInADict(a))
