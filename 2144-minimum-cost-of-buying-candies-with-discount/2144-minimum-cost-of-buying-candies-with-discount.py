class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n=len(cost)
        count=1
        res=0
        for i in range(n-1,-1,-1):
            if count !=3:
                res+= cost[i]
                count+=1
            else:
                count=1
        return res


    

        