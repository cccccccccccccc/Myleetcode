"""
timecomplexity = O(n) spacecomplexity = O(1)
Initialize left pointer to 0 and right pointer to size-1
While left<right, do:
If height[left] is smaller than height[right]
If height[left]≥left_max, update left_max
Else add left_max−height[left] to ans
Add 1 to left.
Else
If height[right]≥right_max, update right_max
Else add right_max−height[right] to ans
Subtract 1 from right.
"""
# from typing import List
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if len(height) <=2:
#             return 0
#         llist = [0]*len(height)
#         rlist = [0]*len(height)  
#         result = 0     
#         for i in range(1,len(height)):
#             llist[i] = max(llist[i-1],height[i-1])
#         for j in range(len(height)-2,0,-1):
#             rlist[j] = max(rlist[j+1],height[j+1])
#         for m in range(1,len(height)):
#             tmp =  min(llist[m],rlist[m])-height[m]
#             if tmp>0:
#                 result+=tmp
#         return result
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        left = 0 
        right = len(height)-1
        water = 0
        while left<right:
            if height[left]< height[right]:
                if height[left]>=leftmax:
                    leftmax = height[left]
                else:
                    water += leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax = height[right]
                else:
                    water+= rightmax-height[right]
                right-=1
        return water

A = Solution()
a = [0,1,0,2,1,0,1,3,2,1,2,1]
print(A.trap(a))
b = [4,2,0,3,2,5]
print(A.trap(b))