class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n=max(nums)
        m=min(nums)
        result=[]
        x=set(nums)

        for i in range(m,n+1):
            if i not in x :
                result.append(i)
                
        return result




        