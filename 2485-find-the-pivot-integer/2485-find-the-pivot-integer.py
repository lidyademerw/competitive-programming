class Solution:
    def pivotInteger(self, n: int) -> int:
        # n(a1 + an)/2  8/2=4, a1=4 --- an=8 if not ,  a1=4+1--an=8 sum=n(a1 + an)/2
        m=1
        while m <= n:
            if m*(1+ m)//2==(n-m+1)*(m+n)//2:
                return m
            m+=1
        return -1    
               
            
        
        