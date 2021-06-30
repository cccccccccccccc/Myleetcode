"""
timecomplexity = O(nlog(n)) n is length of nums
use mergesort 
enumerate nums to list index use for tracking jumps, value use for sorting 

recursion list, get half point separate it into left and right sublist and continue recursion
until half is zero
iterate list to check:
1 if right is null or left is not null and the last element's value in left larger than last element's value in right
use a len(nums) list to record that left last element index that there are len(right)of nums smaller than it  
rewrite i index in iterate as left last element's value
2 else rewrite i index in iterate as right last element's value

after recursion return record list 
"""

from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enums):
            half = len(enums)//2
            if half:
                left, right = sort(enums[:half]),sort(enums[half:])
                for i in range(len(enums))[::-1]:
                    if not right or left and left[-1][1]>right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enums[i] = left.pop()
                    else:
                        enums[i] = right.pop()
            return enums
        smaller = [0]*len(nums)
        sort(list(enumerate(nums)))
        return smaller
A = Solution()
a = [5,2,6,1]
b = [7,1,3,2,9,2,1]
print(A.countSmaller(a))