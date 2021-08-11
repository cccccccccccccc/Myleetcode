"""
timecoplexity = O(n) n is length of s
use dict k is letter value is num of this letter
iterate k in dict
if dict[k] not in frequnecy set add into set
else iterate to decrease get vailable num which does not in set
and add answernum minnum
"""
from collections import defaultdict
from typing import List
class Solution:
    def minDeletions(self, s: str) -> int:
        sdict = defaultdict(int)
        for c in s:
            sdict[c]+=1
        minnum = 0
        frequencyset = set()
        for k in sdict:
            for i in range(sdict[k],0,-1):
                if i not in frequencyset:
                    frequencyset.add(i)
                    break
                else:
                    minnum+=1  
        return minnum
A = Solution()
s = "ceabaacb"
print(A.minDeletions(s))