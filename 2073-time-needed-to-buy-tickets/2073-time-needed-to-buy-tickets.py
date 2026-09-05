class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ticket=deque()
        n=len(tickets)
        for i in range(n):
            ticket.append(i)
        count=0
        while len(ticket)>0:
            x=ticket.popleft()
            tickets[x]-=1
            count+=1
            if k==x and tickets[x]==0:
                return count
            if tickets[x]>0:
                ticket.append(x)





       