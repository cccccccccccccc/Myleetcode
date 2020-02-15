from typing import List
timecomplexity = O(n) spacecomplexity = O(n)
            # I like to explain the part above
            # take the str "PAYPALISHIRING" for example:
            # We start with variable index with the value 0, step with the value 1
            # Each row added with the next char
            # If we reach the bottommost row, we need to turn to the next above row, so we change the step value to -1
            # we keep the step value until we reach topmost row. DON'T CHANGE IT!
            # Again, if we reach the topmost row, we need to reset the step value to 1
            # What we need to remember is:
            # the zigzag pattern is just a pictorial image for us to have a better understanding
            # What the trick of algorithm is actually add the next char of the given string to different rows.
            # Don't really think how to move the cursor in the matrix.
            # It's really misleading way you think of this. Even it works, it's not efficient.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <=1 or len(s) <numRows:
            return s
        strrow = ['']*numRows
        index, step = 0,1
        for x in s:
            strrow[index] += x
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index+=step
            # I like to explain the part above
            # take the str "PAYPALISHIRING" for example:
            # We start with variable index with the value 0, step with the value 1
            # Each row added with the next char
            # If we reach the bottommost row, we need to turn to the next above row, so we change the step value to -1
            # we keep the step value until we reach topmost row. DON'T CHANGE IT!
            # Again, if we reach the topmost row, we need to reset the step value to 1
            # What we need to remember is:
            # the zigzag pattern is just a pictorial image for us to have a better understanding
            # What the trick of algorithm is actually add the next char of the given string to different rows.
            # Don't really think how to move the cursor in the matrix.
            # It's really misleading way you think of this. Even it works, it's not efficient.           
        return ''.join(strrow)
A = Solution()
s = "AB"
print(A.convert(s,1))