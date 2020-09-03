from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <=2:
            return 0
        llist = [0]*len(height)
        rlist = [0]*len(height)  
        result = 0     
        for i in range(1,len(height)):
            llist[i] = max(llist[i-1],height[i-1])
        for j in range(len(height)-2,0,-1):
            rlist[j] = max(rlist[j+1],height[j+1])
        for m in range(1,len(height)):
            tmp =  min(llist[m],rlist[m])-height[m]
            if tmp>0:
                result+=tmp
        return result
A = Solution()
a = [0,1,0,2,1,0,1,3,2,1,2,1]
print(A.trap(a))