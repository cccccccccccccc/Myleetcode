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