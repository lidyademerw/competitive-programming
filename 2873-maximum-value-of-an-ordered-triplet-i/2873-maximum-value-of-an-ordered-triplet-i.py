class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            for j in  range (i+1,n):
                for k in range(j+1,n):
                    x=(nums[i] - nums[j] ) * nums[k]
                    res=max(res,x)
        return res


