class Solution:
    def checkcomparison(self,wordict):
        for k in wordict:
            if k in self.checkdict and wordict[k] <= self.checkdict[k]:
                continue
            else:
                return False
        return True
    def moveleft(self,s,left,right,wordict):
        if left<=right:
            if s[left] in self.checkdict:
                self.checkdict[s[left]] -=1
            left +=1
            if self.checkcomparison(wordict) == True:
                if (right-left+1)<self.length:
                    self.resstr = s[left:right+1]
                    self.length = min(self.length,(right-left+1))
                left = self.moveleft(s,left,right,wordict)
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
            self.checkdict[i] = 0
        left = right = 0
        self.length = float('INF')
        self.resstr = ''
        for right,val in enumerate(s):
            if val in wordict:
                if val not in self.checkdict:
                    self.checkdict[val] = 1
                else: 
                    self.checkdict[val]+=1
                if self.checkcomparison(wordict) == True:
                        if (right-left+1)<self.length:
                            self.resstr = s[left:right+1]
                            self.length = min(self.length,(right-left+1))
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
print(A.minWindow(s3,t1))