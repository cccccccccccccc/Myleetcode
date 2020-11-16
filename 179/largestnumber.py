from typing import List
class LargeNum(str):
    def __lt__(self,others):
        return self+others>others+self
class Solution:
    def largestNumber(self, nums: List[int])->str:
        ansnum=''.join(sorted(map(str,nums),key = LargeNum))
        return '0' if ansnum[0] == '0'else ansnum
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        anslist = []
        maxlen = len(str(max(nums)))

        for n in nums:
            strn = str(n)
            addlen = maxlen - len(strn)
            if addlen >0:
                anslist.append((strn,strn+strn[-1]*addlen))
            else:
                anslist.append((strn,strn))
        anslist.sort(key=lambda x: x[1],reverse=True)
        ans = ""
        for i in anslist:
            ans +=i[0]
        return ans
        """

A = Solution()
a = [34323,3432]
print(A.largestNumber(a))