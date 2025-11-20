class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m=Counter(nums)
        for i in nums:
            if m[i]>1:
                return i
        