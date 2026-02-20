class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()  # [-100,-7,-1,8,100]
        if all(i >= 0 for i in nums):
            return nums[len(nums)-1] *nums[len(nums)-2]*nums[len(nums)-3]
        elif all(i < 0 for i in nums):
            return nums[len(nums)-1] *nums[len(nums)-2]*nums[len(nums)-3]
        else:
            
            return max((nums[0]*nums[1]*nums[-1]) , nums[len(nums)-1] *nums[len(nums)-2]*nums[len(nums)-3])

       
        