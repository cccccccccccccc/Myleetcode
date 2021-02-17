from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapnums = []
        heapq.heapify(heapnums)
        for i in nums:
            if len(heapnums) < k:
               heapq.heappush(heapnums,i)
            elif i > heapnums[0]:
                heapq.heappushpop(heapnums,i)
        return heapnums[0]
A = Solution()
n = [3,2,1,5,6,4]
k = 2
n1=[3,2,3]
k1=2
print(A.findKthLargest(n,k))
print(A.findKthLargest(n1,k1))