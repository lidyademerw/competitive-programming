class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = str(n).replace('0','')
        if not x:
            return 0
        res=0
        for i in x:
            res+=int(i)

        return int(x) * res

        