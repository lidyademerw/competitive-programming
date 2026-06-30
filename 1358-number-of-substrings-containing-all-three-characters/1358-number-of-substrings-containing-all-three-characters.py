class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        n=len(s)
        fm=defaultdict(int)
        res=0
        for r in range(n):
            fm[s[r]]+=1
            while l<r and all(fm[i] > 0  for i in 'abc'):
                fm[s[l]]-=1
                l+=1
                res+=n-r
        return res

                
                



        