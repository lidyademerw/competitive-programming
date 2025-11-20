class Solution:
    def singleNumber(self, nums: List[int]) -> int:

       m=Counter(nums)
       for i in nums:
        if m[i]==1:
            return i
        
        