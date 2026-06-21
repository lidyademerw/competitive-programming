class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum=0
        count=0
        for i in costs:
            if sum<coins and i< coins:
                sum+=i
                if sum<=coins:
                    count+=1
        return count
            
            

        