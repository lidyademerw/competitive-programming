class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        x=[]
        visit=set()
        def dfs(res):
            if len(res)==len(nums):
                x.append(res[:])
                return
            for i in range(len(nums)):
                if i in visit:
                    continue
                res.append(nums[i])
                visit.add(i)
                dfs(res)
                res.pop()
                visit.remove(i)
        dfs([])
        return x
            
           