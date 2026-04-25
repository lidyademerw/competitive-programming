class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        m=[]
        for n in range(left,right +1):
            is_true = True
            for i in str(n):
                x=int(i)
                if x==0 or n%x!=0:
                    is_true=False
                    break
            if  is_true:
                m.append(n)
        return m
           
        
        