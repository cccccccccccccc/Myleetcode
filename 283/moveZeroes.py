from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        zeronum = nums.count(0)
        if zeronum == len(nums):
            return
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
        nums[j:] = [0]*zeronum
        print(nums)
        return
A = Solution()
a = [0,1,0,3,12]
b = [0]
c = [0,0,0]
print(A.moveZeroes(c))