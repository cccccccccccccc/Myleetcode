from typing import List
class Solution:
    def MaxKinarray(self,arrays:List):
        if len(arrays)<2:
            return 0
        arrays.sort()
        if arrays[0]>=0:
            return 0
        checkset = set(arrays)
        i = 0
        while arrays[i]<0:
            if -arrays[i] in checkset:
                return -arrays[i]
            i+=1
        return 0
A = Solution()
a = [1, 2, 3, -4]
print(A.MaxKinarray(a))