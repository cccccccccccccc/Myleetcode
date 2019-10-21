from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]]= i
        m = 0
        while m <len(nums):
            tmp = target - nums[m]
            if tmp in dic and dic[tmp] != m:
                return [m,dic[tmp]]
            m+=1
        return []
A = Solution()
a = [3,2,4]
b = 6
print (A.twoSum(a,b))