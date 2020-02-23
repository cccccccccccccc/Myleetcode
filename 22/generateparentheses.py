"""
Instead of adding '(' or ')' every time as in Approach 1, let's only add them when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
timecomplexity = O(4^n/squrt(n)) spacecomplexity = O(4^n/squrt(n))and O(n) to store the sequence
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(s = '',left = 0,right = 0):
            if len(s) == 2*n:
                ans.append(s)
                return ans
            if left<n:
                backtrack(s+'(',left+1,right)
            if right<left:
                backtrack(s+')',left,right+1)
        backtrack()
        return ans
A = Solution()
a = 3
print(A.generateParenthesis(a))