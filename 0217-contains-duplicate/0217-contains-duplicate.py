class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m=set(nums)
        if len(m)==len(nums):
            return False

        else:
            return True

        