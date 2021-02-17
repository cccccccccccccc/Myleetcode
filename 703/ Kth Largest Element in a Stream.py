from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heaqnums = []
        self.k = k
        heapq.heapify(self.heaqnums)
        for i in nums:
            if len(self.heaqnums)< k:
                heapq.heappush(self.heaqnums,i)
            elif i > self.heaqnums[0]:
                heapq.heappushpop(self.heaqnums,i)
    def add(self, val: int) -> int:
        if len(self.heaqnums) <self.k:
            heapq.heappush(self.heaqnums,val)
        elif val > self.heaqnums[0]:
            heapq.heappushpop(self.heaqnums,val)
        return self.heaqnums[0]

A = KthLargest(2,[0])
print(A.add(-1))
print(A.add(1))
print(A.add(-2))
print(A.add(-1))
print(A.add(3))
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
#["KthLargest","add","add","add","add","add"]
#[[2,[0]],[-1],[1],[-2],[-4],[3]]