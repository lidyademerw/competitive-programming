class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        x=[]
        nums.sort()
        def sub(i,res):
            if i==len(nums):
                x.append(res)
                return
            sub(i+1,res+[nums[i]])
            while i+1<len(nums)and nums[i]==nums[i+1]:
                i+=1
            sub(i+1,res)
        sub(0,[])
        return x
        
            