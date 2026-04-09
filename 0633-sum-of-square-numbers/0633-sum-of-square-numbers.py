class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(sqrt(c))
        while a <= b:
            sumx=pow(a,2) + pow(b,2)
            if sumx==c:
                return True
            elif sumx < c:
                a+=1
            else:
               b-=1
        return False