import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        m=1
        if num<=1:
            return False
        for i in range(2,int(sqrt(num))+1):
            if num%i==0:
                m=m+i
                if i!=num//i:
                    m+=num//i
          
   
        return m==num
      
            

        