"""
timecomplexity = O(klogk) k is depth of heap. spacecomplexity = O(1)
in this case, we need to use more times of the small length than larger length of the sticks. so use heap to construct a min root tree get the two smaller one from heap
head sum them and add to totalcost, push the sum back to heap, until heap has only one inside. return the totalcost.

"""
from typing import List
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        totalcost = 0
        while len(sticks)>1:
            min1 = heapq.heappop(sticks)
            min2 = heapq.heappop(sticks)
            tmpsub= min1+min2
            totalcost += tmpsub
            heapq.heappush(sticks,tmpsub)
        return totalcost
A = Solution()
sticks = [5]
print(A.connectSticks(sticks))