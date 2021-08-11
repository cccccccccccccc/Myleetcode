# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

"""
timecomplexity = O(n)
The first loop is to exclude n - 1 labels that are not possible to be a celebrity candidate.
After the first loop, x is the only candidate camdidate.
because candidate may not be the celebrity in the case of no celebrity at all,The second and third loop is to verify x is actually a celebrity by definition.
The total calls of knows is thus 3n at most. One small improvement is that in the second loop we only need to check i in the range [0, x). You can figure that out yourself easily.
"""

from typing import List
class Solution:
    def findCelebrity(self, n: int) -> int:
        
        candidate = 0
        for i in range(n):
            if knows(candidate,i):
                candidate = i
        for j in range(n):
            if j == candidate:
                continue
            if knows(candidate,j) or knows(j,candidate) != 1:
                return -1
        return candidate

A = Solution()
print(A.findCelebrity(3))