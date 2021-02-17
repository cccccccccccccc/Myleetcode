from typing import List
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = []
        self.larger = []
        heapq.heapify(self.smaller)
        heapq.heapify(self.larger)

    def addNum(self, num: int) -> None:
        if len(self.smaller) == 0:
            heapq.heappush(self.smaller,-num)
            return
        if num > -self.smaller[0]:
            if len(self.smaller) == len(self.larger):
                if num > self.larger[0]:
                    heapq.heappush(self.smaller,-self.larger[0])
                    heapq.heappushpop(self.larger,num)
                else:
                    heapq.heappush(self.smaller,-num)
            else:
                heapq.heappush(self.larger,num)
        elif len(self.smaller) == len(self.larger):
                heapq.heappush(self.smaller,-num)
        elif num == -self.smaller[0]:
            heapq.heappush(self.larger,num)
        else:
            heapq.heappush(self.larger,-self.smaller[0])
            heapq.heappushpop(self.smaller,-num)

    def findMedian(self) -> float:
        if len(self.larger) == len(self.smaller):
            return (-self.smaller[0] + self.larger[0])/2
        else:
            return -self.smaller[0]

A = MedianFinder()
A.addNum(6)
A.addNum(10)
A.addNum(2)
A.addNum(6)
print(A.findMedian())
A.addNum(5)
print(A.findMedian())
A.addNum(0)
print(A.findMedian())
A.addNum(6)
print(A.findMedian())
["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()