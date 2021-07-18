"""
timecomplexity = O(dj^2)
this is a dynamic programming question. 
dp [i][j] the minimum difficulty about 1 to i days to construct 1to j jobs 
the function for this dp problem is 

dp[i][j] = min(dp[i][j],max(dp[i-1][x-1],maxd))
maxd is  the max difficult job between x to j
for x in range(j,i-1,-1)
maxd = max(maxd,jobDifficulty[x-1])
dp[0][0]is padding 0
others is padding 10001

similar with 139 and 472
"""
from collections import defaultdict
from typing import List
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        job= len(jobDifficulty)  
        dp = [[10001 for _ in range(job+1)] for _ in range(d+1)] 
        dp[0][0] = 0
        for i in range(1,d+1):
            for j in range(i,job+1):
                #for x in range(i-1,j):
                maxd = 0
                for x in range(j,i-1,-1):
                    maxd = max(maxd,jobDifficulty[x-1]) # x-1 is for padding
                    dp[i][j] = min(dp[i][j],(dp[i-1][x-1]+maxd)) # day 1...i-1 do job 1...x-1    day i do job x...j

        return dp[d][job]

"""
from typing import List
from collections import defaultdict
class Solution1:
    def _mindifficulty(self,jobDifficulty,dictdp,d,j):
        if (d,j) not in dictdp.keys():
            dictdp[(d,j)] = 10001
            maxd=0
            for x in range(j,d-1,-1):
                maxd = max(maxd,jobDifficulty[x-1])
                dictdp[(d,j)] = min(dictdp[(d,j)],self._mindifficulty(jobDifficulty,dictdp,d-1,x-1)+maxd)
        return dictdp[(d,j)]
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        job= len(jobDifficulty)  
        dictdp = {}
        for i in range(d+1):
            dictdp[(0,i)] = 0
        return self._mindifficulty(jobDifficulty,dictdp,d,job)
"""
A = Solution1()
j = [6,5,4,3,2,1]
#d = 6
d=2
print(A.minDifficulty(j,d))

#[11,111,22,222,33,333,44,444]


'''
cost: 10 20 30
index 1  2   3

max[x] => max{cost[x..3]}

max:
x=1
max1 = max(1, 2, 3)



x=2
max2 = max(2, 3)

max1, cost[1]  =/=> max2



reverse:
max:
x=3
max3 = max(3)



x=2
max2 = max(cost[2], max3)

x=1
max1 = max(cost[1], max2)




'''

