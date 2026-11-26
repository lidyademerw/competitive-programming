class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col=set()
        posdia=set()
        negdia=set()
        x=[]
        border=[["."]*n for _ in range(n)]
        def backtrack(r):
            if r==n:
                x.append(["".join(m) for m in border])
                return
            for c in range(n):
                if c in col or (r-c) in negdia or  (r+c) in posdia:
                    continue
                col.add(c)
                posdia.add(r+c)
                negdia.add(r-c)
                border[r][c]="Q"
                backtrack(r+1)
                col.remove(c)
                posdia.remove(r+c)
                negdia.remove(r-c)
                border[r][c]="."
        backtrack(0)
        return x
       


