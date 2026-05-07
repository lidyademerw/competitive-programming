class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        x1=0
        x2=len(nums)-1
        index=len(nums)-1
        while index>=0:
            if abs(nums[x1])>abs(nums[x2]):
                output[index]=nums[x1]**2
                x1+=1
                index-=1
            else:
                output[index]=nums[x2]**2
                x2-=1
                index-=1
        return output
            



        