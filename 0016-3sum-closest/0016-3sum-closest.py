class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        clos=float('inf')
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            high=len(nums)-1
            low=i+1
            while low < high:
                x=nums[i] + nums[low] + nums[high]
                if abs(x-target) < abs(clos - target):
                    clos=x
                if x==target:
                    return x
                elif x < target:
                    low+=1
                else:
                    high-=1
        return clos





                    


        