from collections import deque
class Solution:
    def getcount(self, dequenum,numdict):
        while len(dequenum) != 0:
            num = dequenum.popleft()
            if num == 0 :
                return numdict[num]
            i = 1
            while i**2 <= num:
                tmp = num-i**2
                if tmp not in numdict:
                    numdict[tmp] = numdict[num]+1
                    dequenum.append(tmp)
                i+=1       
    def numSquares(self, n: int) -> int:
        numdict = {}
        dequenum = deque()
        numdict[n] = 0
        dequenum.append(n)
        return self.getcount(dequenum,numdict)
A = Solution()
print(A.numSquares(13))
