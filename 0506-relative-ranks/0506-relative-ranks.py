class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x=[]
        for i in range(len(score)):
            heapq.heappush(x,(-score[i],i))
        result=[0]*len(score)
        rank=1
        while x:
            score,index=heapq.heappop(x)
            if rank==1:
                result[index] = "Gold Medal"
            elif rank == 2:
                result[index] = "Silver Medal"
            elif rank == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank)
            rank += 1
        return result   

            


        