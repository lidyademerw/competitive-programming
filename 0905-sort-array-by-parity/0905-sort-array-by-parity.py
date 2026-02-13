class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        m=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[m],nums[i]=nums[i],nums[m]
                m+=1
        return nums

        