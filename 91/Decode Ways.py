"""
timecomplexity = O(n) spacecomplexity = O(1)
Fibonacci sequence 
the num can be decoded by one or two num f(n) = f(n-1)+f(n-2) 
if f(n-2) two_digit is between 10 to 26 is ok  if s[i] == '0' f(n-1) can not be use 
so  we can use two variables to store last two result w1 one step back  w2 two step back
init w1 w2 by 1 
iterate 1to len(s)
w = 0 
if s[i] != 0 w = w1 
if two digit in 10 to 26 w+=w2  
shift w2->w1 and w1->w
in the end return w1
"""
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
        return w1
A = Solution()
#print(A.numDecodings("2611055971756562"))
print(A.numDecodings("175"))
