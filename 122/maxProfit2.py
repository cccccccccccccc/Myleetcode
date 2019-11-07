'''
time complexity=O(n) space complexity = O(1) 
sum = every two adjacant numbers' difference
[1,2,3,4,5] 
sum = 2-1 + 3-2 + 4-3 + 5-4
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        buy = prices[0]
        profitsum = 0
        for i in prices[1:]:
            if i > buy:
                profitsum += i-buy
            buy = i
        return profitsum
A = Solution()
a = [7,6,5,4,3,2]    
print(A.maxProfit(a))    
        
