class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        x=Counter(nums)
        def backtrack(res):
            if len(res)==len(nums):
                ans.append(res[:])
                return
            for i in x:
                if x[i]>0:
                    res.append(i)
                    x[i]-=1
                    backtrack(res)
                    x[i]+=1
                    res.pop()
        backtrack([])
        return ans


        