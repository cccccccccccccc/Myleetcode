"""
time complexity O(log(min(n,m)))
k is the medium of merge nums1, nums2
m1+m2 = k 
use binary search 
find 4 elements A[m1-1],A[m1],B[m2-1],B[m2]
l = 0 r = len(min(m,n))
m1 = l+(r-l)//2
m2 = k-m1
if  A[m1] < B[m2-1] means we didn't use enough num from A array
l = m1+1
else
r = m1
get max(A[m1-1],B[m2-1]) and min(A[m1],B[m2]) depend on  m+n is odd or even
"""
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1>n2: return self.findMedianSortedArrays(nums2,nums1)
        k = (n1+n2+1)//2
        l = 0
        r = n1
        while l < r:
            m1 = l+(r-l)//2
            m2 = k-m1
            if nums1[m1]<nums2[m2-1]:
                l = m1+1
            else:
                r = m1
        m1 = l 
        m2 = k-m1
        c0 = max((-10**6 if m1<=0 else nums1[m1-1]),(-10**6 if m2<=0 else nums2[m2-1]))
        if (n1+n2)%2 == 1:
            return c0
        c1 = min((10**6 if m1>=n1 else nums1[m1]),(10**6 if m2>=n2 else nums2[m2]))
        return (c0+c1)*0.5
A = Solution()
n1= []
n2 = [1]
print(A.findMedianSortedArrays(n1,n2))