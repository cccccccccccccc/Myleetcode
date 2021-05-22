"""
timecomplexity = O(4^N*N) complexity = O(N)
N is digits numebers length
"""
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        numtoletter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        def combinations(depth,current):
            if len(digits) == depth:
                res.append(current)
                return
            for i in numtoletter[digits[depth]]:
                combinations(depth+1,current + i)
            
        combinations(0,'')
        return res
A = Solution()
print(A.letterCombinations(''))