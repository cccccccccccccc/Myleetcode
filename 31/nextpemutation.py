"""
from the last element find the first decrement zone: when nums[i]> nums[i-1] 
if the last one is bigger than the one before it ,it is decrement
remenber to check if the whole nums is decrement
from the decrement zone find the min element which is bigger then the one before the decrement zone
and change them 
because the zone is decrement so after change just do reverse is ok

"""
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numslen = len(nums)-1
        if len(nums) <= 1:
            return
        i = numslen
        while i > 0:
            if nums[i] > nums[i-1]:
                break
            i-=1
        if i == numslen: ## only the last element is de
            nums[-1],nums[-2] = nums[-2],nums[-1]
        elif i == 0:
            nums.reverse()
        else:
            m = numslen
            while m > i:
                if nums[m] > nums[i-1]:
                    break
                m-=1
            nums[i-1],nums[m] = nums[m],nums[i-1]   
            nums[i:] = nums[i:][::-1]
            """
            l,r = i,numslen
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            """
        print(nums)
        return

A = Solution()
a = [1,2,3,4]
b = [1,2,4,3]
c = [4,3,2,1]
d = [0]
e = [5,5]
f = []
print(A.nextPermutation(b))