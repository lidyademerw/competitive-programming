class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        max_left=nums[0]
        difference=nums[0]-nums[1]
        for i in range(2,len(nums)):
            res=max(res,difference*nums[i])
            max_left=max(max_left,nums[i-1])
            difference=max(difference, max_left-nums[i])
        return res  

       