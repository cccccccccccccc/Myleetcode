"""
timecomplexity = O(n**2) spacecomplexity = O(n)
seperate these arrays into two group 
one group be the seen nest iterate each item in them example a in nums1 and b in nums2 get seen[a+b] and remain the count 
the other group alse nest iterate each item  for example c in nums3 and d in nums4 and check if -(c+d) in seen if exist cnt += seen[-(d+c)]
return cnt
"""
from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        seen = {}
        cnt = 0
        for a in nums1:
            for b in nums2:
                if a+b in seen.keys():
                    seen[a+b] +=1
                else:
                    seen[a+b] = 1
        for c in nums3:
            for d in nums4:
                if -(c+d) in seen.keys():
                    cnt +=seen[-(c+d)]

        return cnt
A = Solution()
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(A.fourSumCount(nums1,nums2,nums3,nums4))
nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
print(A.fourSumCount(nums1,nums2,nums3,nums4))