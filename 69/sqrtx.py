class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2 :
            return x
        l = 0
        r = x
        while l < r:
            m = l+(r-l)//2
            if m> x/m:
                r = m
            else:
                l = m +1
        return l-1
A = Solution()
a = 3
print(A.mySqrt(a))