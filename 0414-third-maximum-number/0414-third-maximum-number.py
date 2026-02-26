class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m = list(set(nums))
        m.sort()
        if len(m)<3:
            return m[-1]
        else:
            return m[-3]
        