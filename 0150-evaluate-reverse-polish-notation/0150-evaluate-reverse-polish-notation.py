class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(i)
            else:
                        
                    if len(stack)>1:
                        fs=stack.pop()
                        snd=stack.pop()
                        result=f"{snd} {i} {fs}"
                        ans=eval(result)
                        stack.append(int(ans))
        return int(stack[0])


                
        