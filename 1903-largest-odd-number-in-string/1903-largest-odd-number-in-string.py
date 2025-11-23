class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            m = num[i]
            if int(m) % 2 != 0:
                return num[:i+1]
        return ""
            
       
        
            
      

    


        