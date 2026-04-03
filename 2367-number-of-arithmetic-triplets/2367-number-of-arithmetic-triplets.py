class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0 
        x=set(nums)
        for i in nums:
            if i-diff in x and i-2*diff in x:
                count+=1
        return count


