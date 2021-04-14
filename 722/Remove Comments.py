from typing import List
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        code = []
        isInblock = False
        buff = ""
        for s in source:
            s1 = s + " "
            isLastMatched = False
            for i in range(1, len(s1)):
                c = s1[i - 1: i + 1]
                if isLastMatched == False:
                    if isInblock == False:
                        if c == "//":
                            break
                        elif c == "/*":
                            isInblock = True
                            isLastMatched = True
                        else:
                            buff+=s1[i - 1]    
                    else:
                        if c == "*/":
                            isInblock = False
                            isLastMatched = True
                else:
                    isLastMatched = False
                    
            if isInblock ==False:
                if buff != "":
                    code.append(buff)
                    buff = ""
                '''
                if i == len(s)-2 and s[i:] != "*/":
                    buff+=s[i+1]
                if buff != "":
                    code.append(buff)
                    buff = ""
                    '''
                
        return code
A = Solution()
s = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
s1=["a/*comment", "line", "more_comment*/b"]
print(A.removeComments(s))