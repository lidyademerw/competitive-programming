class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        x=[[]]
        for i in nums:
            x+=[list + [i] for list in x]
        return x
          

        