"""
timecomplexity = O(n)
iterate array if i >0 ans*=1 if i<0 ans*=-1 of i==0 return 0
"""
from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
            if i == 0:
                return 0
            elif i>0:
                ans*=1
            else:
                ans*=-1
        return ans
"""
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nums.sort()
        if nums.count(0) >0:
            return 0
        if nums[0] >0:
            return 1
        if nums[-1] < 0:
            if len(nums)%2 == 1:
                return -1
            else:
                return 1
        l = 0 
        r = len(nums)
        
        while l<r:
            mid = l+(r-l)//2
            if nums[mid] < 0:
                if nums[mid+1]> 0:
                    break
                l = mid+1
            else:
                if mid >0 and nums[mid-1]< 0 :
                    mid -=1
                    break
                r = mid    
        return -1 if mid%2 == 0 else 1
A = Solution()
nums = [9,72,34,29,-49,-22,-77,-17,-66,-75,-44,-30,-24]
print(A.arraySign(nums))
"""