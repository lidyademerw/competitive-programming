class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        x=[]
        def comb(i,res):
            if sum(res)==n and len(res)==k:
                x.append(res)
                return
            if len(res)>k:
                return
            if i>9:
                return
            if sum(res)>n:
                return
            comb(i+1,res+[i])
            comb(i+1,res)
        comb(1,[])
        return x

        