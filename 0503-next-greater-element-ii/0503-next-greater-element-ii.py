class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        res=n*[-1]
        for i in range(n):
            while stack and nums[i]> nums[stack[-1]]:
                x=stack.pop()
                res[x]=nums[i]
            stack.append(i)
        for i in range(n):
            while stack and nums[i]> nums[stack[-1]]:
                x=stack.pop()
                res[x]=nums[i] 
                
        return res


                