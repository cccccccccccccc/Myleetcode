
"""
timecomplexity = O(n) spacecomplexity = O(1)
use dictionry to contain the appeared char 
key is char value is index in string
iterate the string when current is in dict change left 
count length 

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)
        dictchar = {}
        length = 0
        left = 0
        for right, val in enumerate(s):
            if val in dictchar:
                if left < dictchar[val]+1:
                    left = dictchar[val]+1
            dictchar[val] = right
            if length < right-left+1:
                length = right-left+1
        return length
A = Solution()
a = "abba"
print(A.lengthOfLongestSubstring(a))