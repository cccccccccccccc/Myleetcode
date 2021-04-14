import heapq
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minnum = []
        heapq.heapify(minnum) 
        numset  = set(nums)
        for n in numset:
            heapq.heappush(minnum,n)
        ans = 1
        while len(minnum)>0:
            if minnum[0]>0:
                if minnum[0] == ans:
                    ans+=1
                else:
                    break
            heapq.heappop(minnum)
        return ans
A = Solution()
nums = [1,2,0]
print(A.firstMissingPositive(nums))