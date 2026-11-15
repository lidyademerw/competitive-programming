class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        x=[]
        def sub(i,res):
            if i==len(nums):
                x.append(res)
                return
            sub(i+1,res)
            sub(i+1,res+[nums[i]])
        sub(0,[])
        return x
          

        