class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        p=0
        count=0
        while len(nums)>p:
            if len(str(nums[p]))%2==0:
                count+=1
            p+=1
        return count


        