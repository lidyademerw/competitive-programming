class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo=10**9 + 7
        if n%2==0:
            even=n//2
            odd=n//2
        else:
            even=(n//2)+1
            odd=n//2
        def power(base,expo):
            if expo==0:
                return 1
            if expo%2==0:
                half=power(base,expo//2)%modulo
                return half*half
            else:
                return base*power(base,expo-1)%modulo
        eventotal=power(5,even)
        oddtotal=power(4,odd)        
        return (eventotal * oddtotal)%modulo
        