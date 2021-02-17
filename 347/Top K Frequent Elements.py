from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k,count.keys(),key = count.get)
A = Solution()
n =[1,1,1,2,2,3]
k =2
print(A.topKFrequent(n,k))