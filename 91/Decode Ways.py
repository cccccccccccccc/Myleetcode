class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] =='0':return 0
        w1 = 1
        w2 = 1
        for i in range(1,len(s)):
            w = 0
            if s[i]=='0':
                w = w1
            two_digit = int(s[i-1:i+1])
            if two_digit >=10 and two_digit<=26:
                w += w2
            w2 = w1
            w1 = w
        return w
A = Solution()
#print(A.numDecodings("2611055971756562"))
print(A.numDecodings("175"))
