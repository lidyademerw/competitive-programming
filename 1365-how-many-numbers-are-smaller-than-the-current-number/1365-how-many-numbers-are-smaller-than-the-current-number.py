class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        res=[]
        for i in range (len(nums)):
            count=0
            for j in range(len(nums)):
                if j!=i and nums[i]>nums[j]:
                    count+=1
                else:
                    continue
            res.append(count)
        return res


        