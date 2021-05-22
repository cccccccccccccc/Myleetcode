# time complexity = O(n^2) space complexity = O(n)
#  first sort the list 
# a plus b plus c equals to 0 means a plus b equals to negative c
# let -c be the target so iterate item in sorted nums when -c is larger than 0  it can not make the equal to a plus b equal to -c if a and b is also postive
# use left right pointers from both side of the others nums  i+1 and len-1 whe nums[l]+nums[r] = -target its one result if less than -target l need to bo add 1 if larger r need sub 1
#  traverse the list: use left right as point notice that no item can be repeated 
#  traverse need skip the same items; left and right point need to skip the same items
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        out = []
        nlen = len(nums)
        for i in range (nlen):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            if nums[i]>0:
                break
            target = nums[i]
            l,r = i+1,nlen-1
            while l<r:
                tmp = nums[l]+nums[r]
                if tmp == -target:
                    out.append ([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while r>l and nums[r] == nums[r+1]:
                        r-=1
                elif tmp <-target:
                    l+=1
                else:
                    r-=1
        return out
A = Solution()
a = [-2,0,1,1,2]
b= [-1, 0, 1, 2, -1, -4]
print(A.threeSum(b))