class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        x=[]
        def comb(i,res):
            if sum(res)==target:
                x.append(res)
                return
            if i>=len(candidates):
                return
            if sum(res)>target:
                return
            comb(i+1,res)
            comb(i,res+[candidates[i]])
        comb(0,[])
        return x
            
        