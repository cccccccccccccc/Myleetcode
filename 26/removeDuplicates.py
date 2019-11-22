'''
time complexity = O(n) space complexity = O(1)
use two points j i  as index
find diff elements 
if same i move  j stay the same
'''
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<= 1:
            return len(nums)
        j = 0
        i = 1
        while i < len(nums):
            if nums[j] != nums[i]:
                nums[j+1] = nums[i]
                j+=1
            i+=1
        print(nums)
        return j+1
A = Solution()        
a = [1,1,2]
b = [0,0,1,1,1,2,2,3,3,4]
print(A.removeDuplicates(b))