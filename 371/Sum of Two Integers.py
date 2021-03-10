class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)
A = Solution()
print(A.getSum(-2,-1))