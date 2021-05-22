# time complexity=O(n) space complexity = O(n) 
#  hash key=nums[i] value = i  through target-nums[i] find if sum is available
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
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict = defaultdict(list)
        for i,v in enumerate(nums):
            numsdict[v].append(i)
        for k in numsdict.keys():
            tmp = target-k
            if tmp in numsdict.keys():
                if tmp == k and len(numsdict[k])>=2:
                    return numsdict[k][0:3]
                return [numsdict[tmp],numsdict[k]]
        
A = Solution()
a = [3,2,4]
b = 6
print (A.twoSum(a,b))