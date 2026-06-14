class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n <= 2:
            return []

        prime = [True] * (n+1)
        prime[0] = prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
        x=[]
        for i in range (2, (n // 2)+1):
            if prime[i] and prime[n-i]:
                x.append([i,n-i])
        return x

        

            
        