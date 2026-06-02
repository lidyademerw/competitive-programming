class Solution:
    def maxFreqSum(self, s: str) -> int:
        x=0
        y=0
        m=['a', 'e', 'i', 'o', 'u']
        for i in s:
            if i in m:
                x=max(x,s.count(i))
            else:
                y=max(y,s.count(i))
        return x + y

                


        