"""
timecomplexity = O(n)
find mid and check if is odd
than iterate to get i and -i 
put all items in answer list
"""
from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1 :
            return [0]
        ans = []
        if n%2 == 1:
            ans.append (0)
        mid = n//2+1 # larger than mid, but add 1 at here. can get better runtime than add 1 in range 
        for i in range(1,mid):
            ans.append(i)
            ans.append(-i)
        return ans
        
        