from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsdict = {}
        maxcount = 1
        majorelement = nums[0]
        for i in nums:
            if i in numsdict:
                numsdict[i]+=1
                if maxcount < numsdict[i]:
                    maxcount = numsdict[i]
                    majorelement = i
            else:
                numsdict[i]=1
        return majorelement 
A = Solution()
a = [3,2,3]
b= [2,2,1,1,1,2,2]
c= [0]
print(A.majorityElement(c))
