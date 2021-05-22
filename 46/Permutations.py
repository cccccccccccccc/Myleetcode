"""
timecomplexity = between O(N!) to O(N*N!) space complexity = O(N!)“Factorial of N”
use dfs to get all the permutations.
define a usedelement array to remind if ith is used in cur permutaion
use index to remind cur permutaion's situation 
while index<len(nums) iterate all the item in nums check if is used if not curpemutaion'sindex is nums[i] remind usedelement and recursive by index+1

"""
from typing import List
class Solution:
    def getpermute(self,nums,index,usedelement,cur):
        if index == len(nums):
            self.permutation.append(cur.copy())
            return
        while index < len(nums):
            for i in range(len(nums)):
                if usedelement[i] == False:
                    usedelement[i] = True
                    cur.append(nums[i])
                    self.getpermute(nums,index+1,usedelement,cur)
                    cur.pop()
                    usedelement[i] = False
            return

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutation = []
        usedelement = [False]*len(nums)
        self.getpermute(nums,0,usedelement,[])
        return self.permutation

A = Solution()
nums = [1,2,3]
print(A.permute(nums))
nums = [0,1]
print(A.permute(nums))
nums = [1]
print(A.permute(nums))