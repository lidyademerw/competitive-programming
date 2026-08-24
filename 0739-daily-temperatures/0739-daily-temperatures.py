class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        answer=[0]*n
        for i in range(n):
            while len(stack)>0 and temperatures[stack[-1]]<temperatures[i]:
                index=stack.pop()
                answer[index]=i-index
            stack.append(i)
        return answer


        