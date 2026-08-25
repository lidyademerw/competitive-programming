class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if i>0:
                stack.append(i)
            else:
                while len(stack)>0 and stack[-1]>0 and i<0:
                    last=stack.pop()
                    if last>abs(i):
                        stack.append(last)
                        break
                    if last==abs(i):
                        break
                else:
                    stack.append(i)
        return stack