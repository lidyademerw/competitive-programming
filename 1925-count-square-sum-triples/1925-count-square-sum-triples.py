class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                c=int(sqrt(pow(i,2) + pow(j,2) + 1))
                if c <= n and pow(c,2)==pow(i,2) + pow(j,2):
                    count+=1
        return count
      
        