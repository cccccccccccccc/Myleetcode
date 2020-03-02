class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2):
            num1,num2 = num2,num1
        numdict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        tmp1 = num1[::-1]
        tmp2 = num2[::-1]
        crt = 0
        newnum = ''
        for i in range(len(tmp2)):
            if numdict[tmp1[i]]+numdict[tmp2[i]]+crt-10 >= 0:
                newnum += str(numdict[tmp1[i]]+numdict[tmp2[i]]+crt-10)
                crt = 1
            else:
                newnum += str(numdict[tmp1[i]]+numdict[tmp2[i]]+crt)
                crt = 0
        for j in tmp1[len(tmp2):]:
            if numdict[j]+crt-10 >= 0:
                newnum += str(numdict[j]+crt-10)
                crt = 1
            else:
                newnum += str(numdict[j]+crt)
                crt = 0
        if crt >0:
            newnum+= str(crt)
        return newnum[::-1]
