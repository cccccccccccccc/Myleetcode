from typing import List
class Solution:
    def tryeat(self, piles,m):
        h = 0 
        for p in piles:
            h+=(p-1)//m +1
        return h
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            m = (l+r)//2
            h = 0
            h = self.tryeat(piles,m)
            if h <= H:
                r = m
            else: 
                l = m + 1
        return l