class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n=len(nums)
        minprefix=[0]*n
        minprefix[0]=nums[0]
        for i in range(1,n):
            minprefix[i]=min(minprefix[i-1],nums[i])
        stack=[]
        for j in range(n-1,-1,-1):
            if nums[j]>minprefix[j]:
                while stack and stack[-1]<=minprefix[j]:
                    stack.pop()
                if stack and stack[-1]<nums[j]:
                    return True
                stack.append(nums[j])
        return False