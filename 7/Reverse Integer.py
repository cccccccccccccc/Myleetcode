class Solution:
    def reverse(self, x: int) -> int:
        strx= ""
        maxnum = str(2**31-1)
        minnum = str(-2**31)
        if x == 0:
            return 0
        if x<0:
            strx = str(x)[1:][::-1]
            if strx >minnum[1:]:
                return 0
            else:
                return -int(strx)
        else:
            strx = str(x)[::-1]
            if strx>maxnum:
                return 0
            else: 
                return int(strx)
   
A = Solution()
x = 10012
print(A.reverse(x))
