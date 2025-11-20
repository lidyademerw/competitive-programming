class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        m=Counter(nums)
        result=[]
        for i in nums:
            if m[i]==1:
                result.append(i)
        return result

        