"""
timecomplexity = O(logn) spacecomplexity = O(1)
if n <0 abs n and x = 1/x
math iterate n  when n > 0 , if n%2 == 1 get now x pow*=x
every time x*x n//2 
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <  0:
            n = -n
            x = 1/x
        pow = 1
        while n:
            if n%2 == 1:
                pow *=x
            n=n//2
            x *=x
        return pow
A =Solution()
x = 2
n = 3
print(A.myPow(x,n))
