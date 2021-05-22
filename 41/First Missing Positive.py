"""
timecomplexity = O(N) spacecomplexiy = O(1)
Check if 1 is present in the array. If not, you're done and 1 is the answer.
If nums = [1], the answer is 2.
Replace negative numbers, zeros, and numbers larger than n by 1s.
Walk along the array. Change the sign of (a-1)th element if you meet number a. Be careful with duplicates : do sign change only once. Use [0,n-1] index save information aboutpresence of [1,n]
Walk again along the array.Use index range(1,n+1) check if nums[index-1] is postive element Return the index.
If on the previous step you didn't find the positive element in nums, that means that the answer is n + 1.
"""
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        if nums == [1]:
            return 2
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        for j in nums:
            a = abs(j)
            nums[a-1] = -abs(nums[a-1])
        for m in range(1,n+1):
            if nums[m-1]>0:
                return m
        return m+1

A = Solution()
# nums = [1,2,0]
# print(A.firstMissingPositive(nums))
# nums = [3,4,-1,1]
# print(A.firstMissingPositive(nums))
nums = [2,1]
print(A.firstMissingPositive(nums))