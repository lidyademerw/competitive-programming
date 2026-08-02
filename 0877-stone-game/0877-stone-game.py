class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        i=0
        j=len( piles)-1
        alice=0
        bob=0
        Alice=True
        while i<=j:
            if piles[i]>piles[j]:
                value=piles[i]
                i+=1
            else:
                value=piles[j]
                j-=1
            if Alice:
                alice+=value
            else:
                bob+=value
        return alice >=bob




      