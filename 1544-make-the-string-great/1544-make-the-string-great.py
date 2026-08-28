class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        n=len(s)
        for i in range(n):
            if len(stack)>0 and stack[-1]!=s[i] and stack[-1].upper()==s[i].upper():
                stack.pop()
            else:
                stack.append(s[i])
          
        return "".join(stack)
                
        