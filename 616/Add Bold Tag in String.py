from typing import List
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        needB = [False]*len(s)
        for w in dict:
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
A = Solution()
s = "abcxyz123"
d = ["abc","123"]
s1="aaabbcc"
d1=["a","b","c"]
s2="qrzjsorbkmyzzzvoqxefvxkcwtpkhzbakuufbpgdkykmojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmweyyzzmgcoiupjnidphvzlnxtcogufozlenjfvokztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm"
d2=["qr","zj","so","rb","km","yz","zz","vo","qx","ef","vx","kc","wt","pk"]
print(A.addBoldTag(s2,d2))