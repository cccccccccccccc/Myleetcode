class Solution:
    def getstr(self,num):            
        if num >=20:
            if num/100 >= 1:
                tmp = self.getstr(num%100)
                if tmp != '':   
                    return self.numdict[num//100] + ' Hundred ' + self.getstr(num%100)
                else:
                    return self.numdict[num//100] + ' Hundred'        
            elif self.numdict[num%10] !='':
                return self.numdict[num//10*10]+' '+ self.numdict[num%10]
            else:
                return self.numdict[num//10*10]
        else:
            return self.numdict[num]
    def numberToWords(self, num: int) -> str:
        self.numdict = {0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five', 6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',
                        18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
        billon = 0
        millon = 0
        thousand = 0
        res_str = ''
        if num == 0:
            return 'Zero'
        billon = num//(10**9)
        if billon != 0:
            strbillon = self.getstr(billon)
            res_str+= strbillon + ' Billion'
        millon = (num-billon*10**9)//(10**6)
        if millon != 0:
            strmillon = self.getstr(millon)
            res_str+= ' '+ strmillon+ ' Million'
        thousand = (num-billon*10**9-millon*10**6)//(10**3)
        if thousand != 0:
            strthousand = self.getstr(thousand)
            res_str+= ' '+ strthousand+ ' Thousand'
        underthousand = num%(10**3)
        if underthousand != 0:
            strunder = self.getstr(underthousand)
            res_str+= ' '+ strunder    
        return res_str.strip()
A = Solution()
a = 100
'''1000
1000000
1000000000
1000001'''
print(A.numberToWords(a))