from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return
        m = n/2
        i = 0
        while i < m:
            j= 0
            while j < n:
                matrix[i][j] , matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
                j+=1
            i+=1
        i = 0
        while i < n:
            j = i+1
            while j < n:
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j] 
                j += 1
            i += 1
        print(matrix)
        return
A=Solution()
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]        
b = [[0]]            
print(A.rotate(a))