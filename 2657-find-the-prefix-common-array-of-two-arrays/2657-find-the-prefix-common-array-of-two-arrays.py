class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        a=set()
        b=set()
        both=set()
        res=[]
        for i in range(n):
            a.add(A[i])
            b.add(B[i])
            if A[i] in b:
                both.add(A[i])
            if B[i] in a:
                both.add(B[i])
            res.append(len(both))
        return res



        