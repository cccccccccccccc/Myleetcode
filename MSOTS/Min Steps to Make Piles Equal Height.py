from typing import List
from collections import defaultdict
class Solution:
    def minSteptomakeequal(self,piles:List ):
        if len(piles) <= 1:
            return 0
        pilesdict = defaultdict(int)# value count of the same height
        for i in piles:
            pilesdict[i]+=1
        heightlist = []
        for k in pilesdict:
            heightlist.append(k)
        if len(heightlist) == 1:
            return 0
        heightlist.sort()
        ans = 0
        for i in range(1,len(heightlist)):
            ans+= i*pilesdict[heightlist[i]]
        return ans

A = Solution()
p = [5,5,5,2,2,2,1]
print(A.minSteptomakeequal(p))