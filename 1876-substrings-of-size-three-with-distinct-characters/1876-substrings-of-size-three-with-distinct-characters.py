class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            x=s[i:i+3]
            if len(set(x))==3:
                res+=1
        return res  
        