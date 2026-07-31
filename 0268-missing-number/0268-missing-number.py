class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set1=set(nums)
    
        for i in range(0,len(nums)+1):
            if i not in set1:
               return i
            
            

        