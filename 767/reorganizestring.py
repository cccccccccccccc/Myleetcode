from typing import List
class Solution:
    def reorganizeString(self, S: str) -> str:
        N = len(S)
        A = []
        for c, x in sorted((S.count(x),x) for x in set(S)):
            if c> (N+1)/2:
                return""
            A.extend(c*x)
        ans=[None]*N
        ans[::2],ans[1::2]=A[int(N/2):],A[:int(N/2)]
        return "".join(ans)

A = Solution()
s= "aabbb"
print(A.reorganizeString(s))