class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        x=[]
        candidates.sort()
        def comb(i,res):
            if sum(res)==target:
                x.append(res)
                return
            if sum(res)>target:
                return
            if i>=len(candidates):
                return
        
            comb(i+1,res+[candidates[i]])
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            comb(i+1,res)
        comb(0,[])
        return x
        