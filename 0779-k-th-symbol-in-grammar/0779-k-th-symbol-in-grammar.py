class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        current=0
        r=2**(n-1)
        l=1
        while l<r:
            mid=(r+l)//2
            if k<=mid:
                r=mid
            else:
                l=mid+1
                current=0 if current else 1
        return current


