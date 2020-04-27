"""
DP
dp[i] : Max money after "visiting" house[i]
dp[i] = max(dp[i-2]+money[i],dp[i-1])

"""
#timecomplexity = O(n) spacecomplexity = O(n)->O(1)
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        moneydp = [0]*(len(nums)+1)
        moneydp[1] = nums[0]
        for i in range(2,len(nums)+1):
            moneydp[i] = max(moneydp[i-2]+nums[i-1],moneydp[i-1])
        return moneydp[-1]
A = Solution()
a = [1]
print(A.rob(a))
