from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0=cur = 0
        p1 = len(nums)-1
        while cur <=p1:
            if nums[cur] == 0:
                nums[p0],nums[cur] = nums[cur],nums[p0]
                p0+=1
                cur+=1
            elif nums[cur]==2:
                nums[p1],nums[cur] = nums[cur],nums[p1]
                p1-=1
            else:
                cur+=1
        return nums
A = Solution()
a = [2,0,2,1,1,0]
print(A.sortColors(a))