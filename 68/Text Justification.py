"""
timecomplexity = O(n*m) n is len(words)m is the number of words in each line. spacecomlexity = O(k) k is total len include words and extra " " add to justify maxlength.
iterate all the word in words by index
define start end and curlen
check if cur word can be add into curline, and use function to add " " between words 
first get total number of the space totalb
then check count of words in these line is more than 1 if end is not the last words get per space between words by divide  
if end is last words can just add extra space in the end 
if count is 1 just get all the space in the end 
"""
from typing import List
class Solution:
    def getfulljustify(self,words,start,end,curlen,maxWidth):
        curstr = ""
        count = end-start
        curlen = curlen-count-1
        totalB = maxWidth-curlen
        if count>0:
            if end == len(words)-1:
                j = start
                while j< end:
                    curstr+= words[j]+" "
                    j+=1
                curstr+= words[j]+(" ")*(totalB-count)
                return curstr
            perB = totalB//count
            AddB = totalB%count
            j = start
            while j<end:
                curstr += words[j]+(" ")*perB
                if AddB>0:
                    curstr+=" "
                    AddB-=1
                j+=1
            curstr+= words[j]
        else:
            curstr+= words[start]+(" ")*(maxWidth-len(words[start]))
        return curstr

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if len(words) == 0:
            return [(" ")*maxWidth]
        start = 0
        end = 0
        ans = []
        curlen = 0
        i=0
        while i < len(words):
            if len(words[i])+curlen+1<= maxWidth+1:
                curlen+=len(words[i])+1
                end = i
                i+=1
            else:
                ans.append(self.getfulljustify(words,start,end,curlen,maxWidth))
                start = end = i
                curlen = 0
        if curlen>0:
            ans.append(self.getfulljustify(words,start,end,curlen,maxWidth))
        return ans
A = Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print(A.fullJustify(words,maxWidth))