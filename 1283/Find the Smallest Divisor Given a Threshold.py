from typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = 10**6
        while l < r:
            divisor = l +(r-l)//2
            sum = 0
            for i in nums:
                sum+=((i//divisor+1) if i%divisor>0 else i//divisor)
            if sum <=threshold:
                r = divisor
            else:
                l= divisor+1
        return l
A = Solution()
nums = [1,2,3]
threshold = 6
print(A.smallestDivisor(nums,threshold))