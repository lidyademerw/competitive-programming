class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r=1
        if  target in nums:
            return(nums.index(target))
        if nums[len(nums)-1]<target :
                return len(nums)
        if nums[0]> target:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i]< target and nums[r]>target:
                    return r
                r+=1
        
            

        
        