class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue=deque()
        for i in range(1,n+1):
            queue.append(i)
        count=0
        while len(queue)>1:
            x=queue.popleft()
            count+=1
            if count!=k:
                queue.append(x)
            else:
                count=0
        return queue[0]
       



        