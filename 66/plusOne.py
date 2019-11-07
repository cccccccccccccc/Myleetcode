'''
time complexity=O(n) space complexity = 0 
'''
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> int:
        for i in reversed(range(len(digits))):
            if (digits[i]==9):
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        return [1]+digits
A = Solution()
a = [9,9,9,9,9,9]
print(A.plusOne(a))