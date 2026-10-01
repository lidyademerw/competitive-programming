class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack=[]
        n=len(prices)
        res=[i for i in prices]
        for i in range(n):
            while stack and  prices[i]<=prices[stack[-1]]:
                res[stack[-1]]=prices[stack[-1]]-prices[i]
                stack.pop()
            stack.append(i)    
        return res
            

        