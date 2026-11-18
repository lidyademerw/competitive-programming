class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        x=[]
        def comb(i,res):
            if len(res)==k:
                x.append(res)
                return 
            if i>n:
                return
            comb(i+1,res+[i])
            comb(i+1,res)
        comb(1,[])
        return x
        