from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderdict = {c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1),len(word2))):
                if word1[j] != word2[j]:
                    if orderdict[word1[j]]>orderdict[word2[j]]:
                        return False  
                    break
            else:             
                if len(word1)>len(word2):
                    return False
        return True
A = Solution()
words = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
order ="zkgwaverfimqxbnctdplsjyohu"
w= ["hello","leetcode"]
o = "hlabcdefgijkmnopqrstuvwxyz"
w1 = ["apple","app"]
o1 = "abcdefghijklmnopqrstuvwxyz"
print(A.isAlienSorted(w,o))