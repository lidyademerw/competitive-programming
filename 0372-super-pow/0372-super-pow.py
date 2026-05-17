class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
            res=""
            for i in b:
                res+=str(i)
            x=pow(a,int(res),1337)
            return x

        