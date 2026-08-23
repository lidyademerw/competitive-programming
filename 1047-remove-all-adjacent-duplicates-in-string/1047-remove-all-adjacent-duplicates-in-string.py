class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        n=len(s)
        for i in s:
            if len(stack)>0 and i==stack[-1]:
                stack.pop()
            else:
                stack.append(i)

            

        return "".join(stack)
        