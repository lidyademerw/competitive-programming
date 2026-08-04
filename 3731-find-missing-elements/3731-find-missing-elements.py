class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n=max(nums)
        m=min(nums)
        result=[]

        for i in range(m,n+1):
            if i not in set(nums):
                result.append(i)
                
        return result




        