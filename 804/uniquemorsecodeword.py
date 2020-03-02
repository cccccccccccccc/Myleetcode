from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseform = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        uniqueset = set()
        for word in words:
            tmp = ''
            for i in word:
                tmp += morseform[ord(i)-ord('a')]
            uniqueset.add(tmp)
        return len(uniqueset)
A = Solution()
words = ["gin", "zen", "gig", "msg"]
print(A.uniqueMorseRepresentations(words))
