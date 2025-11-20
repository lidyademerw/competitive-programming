class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       nums.sort()
       result=nums[(len(nums)//2)]
       return result
       


    
                


        