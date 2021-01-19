from typing import List
import random
class Solution:

    def __init__(self, w: List[int]):
        sumweight = 0
        self.wrange = [0]
        for i in range(len(w)):
            self.wrange.append (sumweight+w[i])
            sumweight+=w[i]

    def pickIndex(self) -> int:
        randomnum = random.choice(range(self.wrange[-1]))
        l = 0
        r = len(self.wrange)-1
        while l < r:
            m = l+(r-l)//2
            if self.wrange[m]>randomnum:
                r = m
            else:
                l = m+1
        return l-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()