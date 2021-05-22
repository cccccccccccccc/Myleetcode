"""
timecomplexity = O(|s|+|t|) iterate s  and check left to right is length can be t
spacecomplexity = O(|s|+|t|) the return str maximun can be length of s and the dict is length of t

First use a dict to remainder all the letter and its count appear in t 
use a check dict to mark the letter in t who has appeared in cur substring in s
left right use to mark substring's left and right 
substringlength to cmp each time's substring length help to can the minimun length 
iterate s by index and val  
when the val in dict check if left can be move run subfunction 
in subfunction  iterate to check if we get the minwindow if true remainder cur str and length and shift left add 1 if s[left] in checkdict remainder to del 1 

"""
class Solution:
    def checkcomparison(self,wordict):
        for k in wordict:
            if k in self.checkdict and wordict[k] <= self.checkdict[k]:
                continue
            else:
                return False
        return True
    def moveleft(self,s,left,right,wordict):
        while left<=right:
            if self.checkcomparison(wordict) == True:
                if (right-left+1)<self.length:
                    self.resstr = s[left:right+1]
                    self.length = right-left+1
                if s[left] in self.checkdict:
                    self.checkdict[s[left]] -=1
                left +=1
            else:
                break
        return left
    def minWindow(self, s: str, t: str) -> str:
        if s == '' or t == '':
            return ''
        wordict = {}
        for i in t:
            if i in wordict:
                wordict[i]+=1
            else:
                wordict[i] = 1
        self.checkdict = {}
        for j in wordict.keys():
            self.checkdict[j] = 0
        left = right = 0
        self.length = float('INF')
        self.resstr = ''
        for right,val in enumerate(s):
            if val in wordict:
                self.checkdict[val]+=1
                left = self.moveleft(s,left,right,wordict)

        return self.resstr           
A = Solution()
s = "ADOBECODEBANC"
t = "ABC"
s1 = "ADOBECABANC"
t1 = "ADOBECABANC"
s2 = ""
s3 = "AAAA"
t3 = "AAA"
print(A.minWindow(s,t))