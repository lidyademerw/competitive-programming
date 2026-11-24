class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res=[]
        board=[["."]*n for i in range(n)]
        col=set()
        posdia=set()
        negdia=set()
        def backtrack(row):
            if row==n:
                ans=[]
                for r in board:
                    ans.append("".join(r))
                res.append(ans)
            for c in range(n):
                if  c in col or (row-c) in negdia or (row+c) in posdia:
                    continue
                board[row][c]="Q"
                col.add(c)
                posdia.add(row+c)
                negdia.add(row-c)
                backtrack(row+1)
                board[row][c]="."
                col.remove(c)
                posdia.remove(row+c)
                negdia.remove(row-c)
        backtrack(0)
        return res
                


