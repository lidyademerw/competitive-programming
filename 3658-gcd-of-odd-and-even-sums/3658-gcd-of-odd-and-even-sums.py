class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        odd=1
        even=0
        count=0
        sumodd=0
        sumeven=0
        while count < n:
            odd+=2
            sumodd+=odd
            even+=2
            sumeven+=even
            count+=1
        return math.gcd(sumeven,sumodd)
        