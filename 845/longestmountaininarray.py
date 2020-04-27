#timecomplexity = O(n),spacecomplexity = O(n)
"""
from left do iterate to count, if A[i]>A[i-1] inc count,
from right do iterate to count f A[i]>A[i+1] dec count,
then iterate S to get maximum ans l[i]+r[i]+1
remember to be mountain need both l,r > 0
if only increase or decrease is not mountain
"""
from typing import List
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        l = [0]*len(A)
        r = [0]*len(A)
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                l[i] = l[i-1]+1
            else:
                l[i] = 0
        for j in range(len(A)-2,-1,-1):
            if A[j]>A[j+1]:
                r[j] = r[j+1]+1
            else:
                r[j] = 0
        ans = 0
        for i in range(len(A)):
            if l[i] !=0 and r[i] != 0:
                ans = max(ans,l[i]+r[i]+1)
        return ans
A = Solution()
a = [2,1,4,7,3,2,5]
b =  [2,2,2]
c = [1,2,3]
print(A.longestMountain(c))