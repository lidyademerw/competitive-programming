class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cunt=0
        sell=1
        buy=0
        while sell<len(prices):
            if prices[buy] <prices[sell]:
                diff=prices[sell] - prices[buy]
                cunt=max(cunt,diff)
            else:
                buy=sell
            sell+=1
                
        return cunt
            
            

       

            

        
