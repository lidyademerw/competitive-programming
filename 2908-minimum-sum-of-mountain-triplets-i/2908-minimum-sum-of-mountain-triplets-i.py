class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        total=float('inf') 
        x=False
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] < nums[j] and nums[j]>nums[k]:
                        sumx=nums[i] + nums[j] + nums[k]
                        if sumx < total:
                            total=sumx
                            x=True
                    
      
                    
        return total if x else -1
    