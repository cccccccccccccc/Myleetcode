"""
Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.
timecomplexity = O(N^(t/m+1)) spacecomplexity = O(T/m)
we can use dfs method which implemented with recursion
define the recursive with candidates index target and curarray if target is 0 mean we found a kind of combination and can add to the finallist
else, iterate from index to the len(candidates) if candidates[i]<target can add in cur combination and keep on recursive change target and index to be curvalue
remember to pop cur value from combination after recursive to get more try .
"""
from typing import List
class Solution:
    def dfs(self,nums,s,target,cur):
        if target == 0:
            self.ans.append(cur.copy())
            return
        for i in range(s,len(nums)):
            if nums[i] > target:
                break
            cur.append(nums[i])
            self.dfs(nums,i,target-nums[i],cur)
            cur.pop()
        return
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.dfs(candidates,0,target,[])
        return self.ans
A = Solution()
a = [2,3,6,7]
print(A.combinationSum(a,7))
