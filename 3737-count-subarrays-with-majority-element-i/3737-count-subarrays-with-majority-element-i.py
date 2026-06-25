class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            t=0
            for j in range (i,n):
                if nums[j]==target:
                    t+=1
                if t>(j-i+1)//2:
                    res+=1
        return res

        