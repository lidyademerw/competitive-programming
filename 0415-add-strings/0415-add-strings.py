class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=""
        carry=0
        i=len(num1)-1
        j=len(num2)-1
        while i >=0 or j>=0 or carry:
            d1 = int(num1[i]) if i >= 0 else 0
            d2=int(num2[j])if  j>=0 else  0
            su=d1+d2+carry
            carry=su//10
            digit=su%10
            res= str(digit) + res
            i-=1
            j-=1
        return res    

        