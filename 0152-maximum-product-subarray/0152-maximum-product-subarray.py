class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        min_val=1
        max_val=1
        for i in nums:
            if i==0:
                min_val=1
                max_val=1
                continue
            x=i*max_val
            max_val=max(i*max_val,i*min_val,i)
            min_val=min(x,i*min_val,i)
            res=max(res,max_val)
        return res