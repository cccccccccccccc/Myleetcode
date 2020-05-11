from typing import List
class Solution:
    def isValid(self, s: str) ->bool:
        count = 0
        for i in s:
            if i == '(':
                count+=1
            if i == ')':
                count -=1
            if count< 0:
                return False
        return count == 0
    def dfs(self,s: str,start: int,l: int,r: int,ans: List[str]):
        if l == 0 and r == 0:
            if self.isValid(s):
                ans.append(s)
                return
        for i in range(start,len(s)):
            if i != start and s[i] == s[i-1]:
                continue
            if s[i] == ')' and r>0:               
                tmpstr = s[0:i]+s[i+1:]
                self.dfs(tmpstr,i,l,r-1,ans)
            if s[i] == '(' and r == 0 and l > 0:
                tmpstr = s[0:i]+s[i+1:]
                self.dfs(tmpstr,i,l-1,r,ans)
        return
                
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        l = 0 
        r = 0
        start = 0
        if self.isValid(s) == True:
            ans.append(s)
            return ans
        for i in s:
            if i == '(':
                l +=1
            if i == ')':
                if l == 0:
                    r+=1
                else:
                    l-=1
        self.dfs(s,start,l,r,ans)
        return ans
A = Solution()
a = "()())()"
b=")("
c= "x("
print(A.removeInvalidParentheses(c))