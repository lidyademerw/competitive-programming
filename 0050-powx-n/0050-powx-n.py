class Solution:
    def myPow(self, x: float, n: int) -> float:
       
        def power(x,n):
            if n==0:
                return 1
            res=power(x,n//2)
            if n%2==0:
                return res*res
            else:
                return x*res*res
        ans=power(x,abs(n))
        return ans if n>=0 else 1/ans 

      