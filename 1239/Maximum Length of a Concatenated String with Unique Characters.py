from typing import List
class Solution:
    def isValidStr(self,s):
        tmpset = set()
        for m in s:
            if m in tmpset:
                return False
            else:
                tmpset.add(m)
        return True
    def getmaxLength(self, arr, subarr,i):
        if i >= len(arr):
            self.maxlen = max(self.maxlen,len(subarr))
            return
        tmpstr = arr[i]
        isOk = True
        for s in tmpstr:
            if s in subarr:
                isOk = False
                break
        if isOk:              
            self.getmaxLength(arr,subarr+tmpstr,i+1)
        self.getmaxLength(arr,subarr,i+1)
        return
    def maxLength(self, arr: List[str]) -> int:
        if len(arr) ==0:
            return 0
        newarr = []
        for s in arr:
            if self.isValidStr(s):
                newarr.append(s)
        self.maxlen = 0
        self.getmaxLength(newarr,'',0)
        return self.maxlen
A = Solution()
a = ["un","iq","ue"]
b = ["yy","bkhwmpbiisbldzknpm"]
print(A.maxLength(b))
