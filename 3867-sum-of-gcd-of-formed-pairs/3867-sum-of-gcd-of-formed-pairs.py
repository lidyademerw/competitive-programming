class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        mxi=[nums[0]]*n
        prefixGcd=[nums[0]]*n
    
        for i in range(1,n):
            mxi[i]= max(mxi[i-1],nums[i])
            prefixGcd[i]= gcd(mxi[i],nums[i])  
        x=prefixGcd.sort()
        y=0
        for i in range(n//2):
            y+=gcd(prefixGcd[i],prefixGcd[n-1-i])
            
        return y


        

        