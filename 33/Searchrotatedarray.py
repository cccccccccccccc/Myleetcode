
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0:
            return -1
        l , r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            if nums[l] < nums[m]:
                if nums[l] <= target and nums[m] > target:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] < target and nums[r-1] >= target:
                    l = m + 1
                else:
                    r = m
        return -1

A = Solution()
a = [4,5,6,7,0,1,2]
b = [3,1]
'''
print(A.search(a,1))
print(A.search(a,4))
print(A.search(a,17))
print(A.search(a,7))
print(A.search(a,0))
print(A.search(a,2))
print(A.search(a,3))
print(A.search(a,-1))
'''
print(A.search(b,1))


