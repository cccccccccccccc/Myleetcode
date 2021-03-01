"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        for i in range(2**n,2**(n+1)):
            bitmask = bin(i)[3:]
            output.append([nums[j]for j in range(n) if bitmask[j] == '1'])
        return output
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        cursubset = []
        def dfs(nums,depth,cursubset,output):
            if len(nums) == depth:
                output.append(cursubset.copy())
                return
            dfs(nums,depth+1,cursubset,output)
            cursubset.append(nums[depth])
            dfs(nums,depth+1,cursubset,output)
            cursubset.pop()
        dfs(nums,0,cursubset,output)
        return output
A = Solution()
nums = [1,2,3]
print(A.subsets(nums))
