class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        stack=[]
        count=Counter()
        res=0
        for i in nums:
            while len(stack)>0 and stack[-1]>i:
                count[stack.pop()]-=1
            res+=len(stack)-count[i]
            stack.append(i)
            count[i]+=1
          
        return res
       