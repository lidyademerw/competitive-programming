class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i=0
        j=1
        dis=-1
        while j < len(nums):
            if nums[i]<nums[j]:
                dis=max(dis,nums[j]-nums[i])
            else:
                i=j
            j+=1
        return dis
       