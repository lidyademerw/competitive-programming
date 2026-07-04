class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        res=0
        for i in nums:
            if res<0:
                res=0
            res+=i
            maxsub=max(maxsub,res)
        return maxsub
        