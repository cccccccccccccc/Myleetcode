from typing import List
class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        needB = [False]*len(s)
        for w in words:
            b = 0
            while s.find(w,b) != -1:
                b = s.find(w,b)
                for i in range(len(w)):
                    needB[i+b] = True
                b+=1
        answerstring = ""    
        for j in range(len(s)):
            if needB[j] == False:
                answerstring+=s[j]
            else:
                if j==0 or needB[j-1] == False:
                    answerstring+="<b>"
                answerstring+=s[j]
                if j == len(s)-1 or needB[j+1] == False:
                    answerstring+="</b>"
        return answerstring