class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        m=['a', 'e', 'i', 'o', 'u']
        v=0
        c=0
        for i in s:
            if i in m:
                v+=1 
            elif i.isalpha():
                c+=1
        if c > 0:
            return v//c
        else:
            return 0


        