class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # (a + b) / 2 * k == n, [a, b] has k numbers
        # b == a + k - 1
        # a = (2 * n - k * k + k) / (2 * k)
        count = 0
        for k in range(1, N+1):
            # x should be integer
            if 2*N - k*k+k<=0:
                break
            if (N - k * (k + 1) // 2) % k == 0:
                count += 1
        return count 
A = Solution()
print(A.consecutiveNumbersSum(1))