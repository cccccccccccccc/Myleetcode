from typing import List
class Solution:
    def modifyString(self, s: str) -> str:
        choose = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        l = '1'
        r = ''
        ans =""
        for i in range(len(s)):
            if i==0:
                l = '1'
            else:
                l = ans[i-1]
            if i == len(s)-1:
                r = '1'
            else:
                r = s[i+1]
            if s[i] != '?':
                ans+=s[i]
            else:
                for m in choose:
                    if m != l and m != r:
                        ans+= m
                        break
        return ans
A = Solution()
s = "?a?ub???w?b"
print(A.modifyString(s))