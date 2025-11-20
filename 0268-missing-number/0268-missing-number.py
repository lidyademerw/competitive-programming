class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_1=set(nums)
    
        for i in range(0,len(nums)+1):
            if i not in set_1:
               return i
            
            

        