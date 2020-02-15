""""
timecomplexity = O(n) spacecomplexity = O(1)

"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <=1:
            return 
        l,r = 0,len(s)-1
        while l <= r:
            s[l] ,s[r] = s[r],s[l]
            l+=1
            r-=1
        return
        #Approach 2 
        s.reverse()