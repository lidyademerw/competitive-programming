class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        posdia=set()
        negdia=set()
        border=[["."]*n for _ in range(n)]
        self.res=0
        def backtrack(r):
            if r==n:
                self.res+=1
                return 
            for c in range(n):
                if c in col or (r-c) in negdia or (r+c) in posdia:
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
        return self.res


        