"""
timecomplexity = O(n**3) spacecomplexity = O(n)
the same idea with 3sum 
first check  if length of nums is larger than 4 
sort the nums 
iterate j range is(0,len-2) and make sure nums[j]!= nums[j-1]
inside interate i range is (j+1 ,len-1 )also make sure nums[i]!= nums=[i+1]
then use pointer l from i+1 r from len-1 check sum = nums[j]+nums[i]+nums[l]+nums[r]-target if equal to 0
if equal its one of the result
shift l to l+1 r to r-1 
and make sure after move nums[l]!= nums[l-1] if not keep on move the index
r is the same 
if sum <0 l+1
if sum >0 r-1 
until the end
"""
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)< 4:
            return []
        nums.sort()
        n = len(nums)
        result = []
        for j in range(n-2):
            if j>0 and nums[j] == nums[j-1]:
                continue
            for i in range(j+1,n-1):
                if i >j+1 and nums[i] == nums[i-1]:
                    continue
                l = i+1
                r = n-1
                while l < r:
                    sumnum = nums[j]+nums[i]+nums[l]+nums[r]-target
                    if sumnum == 0:
                        result.append([nums[j],nums[i],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l < r and nums[l]== nums[l-1]:
                            l+=1
                        while l < r and nums[r] == nums[r+1]:
                            r-=1
                    elif sumnum < 0:
                        l+=1
                    else:
                        r-=1
        return result
A = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(A.fourSum(nums,target))