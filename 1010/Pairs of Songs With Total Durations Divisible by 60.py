from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        timedict = {}
        for t in time:
            if t in timedict.keys():
                timedict[t] +=1
            else:
                timedict[t] = 1
        n = 17
        ans = 0
        for i in range(1,n):
            sum = 60*i
            for t in time:
                another = sum-t
                if another in timedict:
                    if another!=t:
                        ans +=timedict[another]
                    else:
                        ans += timedict[another]-1
        return ans//2
A = Solution()
time = [60,60,60]
print(A.numPairsDivisibleBy60(time))
time = [30,20,150,100,40]
print(A.numPairsDivisibleBy60(time))
'''
(a+b)%60 = 0
-->
((a%60)+(b%60))%60 = 0
-->
a%60 = 0 and b% 60 = 0
or 
a%60+ b%60 = 60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
        return ret
'''
