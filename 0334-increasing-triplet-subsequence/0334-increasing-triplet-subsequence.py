class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        nu1=float("inf")
        nu2=float("inf")
        for i in nums:
            if i<=nu1:
                nu1=i
            elif i<=nu2:
                nu2=i
            else:
                return True
        return False
    
            
            

       