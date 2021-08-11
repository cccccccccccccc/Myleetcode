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
"""
timecomplexity = O(t) length of time, 
moudle all time by 60 put the result into a list length is 60
than iterate num from 0 to 30 
if num is 0 or 30 mean there are two same time sum, so we need to make sure they are not sum with themself and the result should be divide by 2
other 1 to 29  we can calculate them just by product i with 60-i  

"""
class Solution1:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        timelist = [0]*60
        for t in time:
            timelist[t%60]+=1
        ans = 0
        for i in range(31):
            if i == 0 or i == 30:
                ans+= (timelist[i]*(timelist[i]-1))//2
            else:
                ans+=timelist[i]*timelist[60-i]
        return ans        
A = Solution1()
#time = [60,60,60]
#print(A.numPairsDivisibleBy60(time))
time = [3,2,15,10,4]
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
