class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        if len(num)==k:
            return "0"
        for i in num:
            while k>0 and stack and  stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        while k>0:
            stack.pop()
            k-=1   
        res= "".join(stack).lstrip("0")
        return res  if res else "0"


        