class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #[1,2,3,4] (1,2)+(2,3)+(3,4)+(4,1)
        nums.sort() #[1,2,3,4]
        count=0
        for i in range(0,len(nums),2):
            count+=nums[i]
        return count


        