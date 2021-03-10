class Solution:
    def isValid(self,c):
        return 1 if c != '0' else 0
    def isValidTwo(self,c1,c2):
        if c1 == '0': return 0
        if int(c1+c2)<=26 :
            return 1
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] =='0':return 0
        if len(s)==1:
            return 1 if s[0] != '0'else 0
        w1 = 1
        w2 = 1
        for i in range(1,len(s)):
            w = 0
            if not(self.isValid(s[i])) and not(self.isValidTwo(s[i-1],s[i])):
                return 0
            if self.isValid(s[i]):
                w = w1
            if self.isValidTwo(s[i-1],s[i]):
                w+=w2
            w2 = w1
            w1 = w
        return w1
A = Solution()
#print(A.numDecodings("2611055971756562"))
print(A.numDecodings("175"))
