class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum=sum(nums[:k])
        maxSum=sum(nums[:k])
        for i in range(len(nums)-k):
            currentSum+=nums[i + k] - nums[i]
            maxSum=max(maxSum,currentSum)
        return maxSum/k
        