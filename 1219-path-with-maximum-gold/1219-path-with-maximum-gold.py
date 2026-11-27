class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visit=set()
        def backtrack(r,c):
            if r<0 or r>=row or c<0 or c>=col or (r,c) in visit or grid[r][c]==0:
                return 0
            visit.add((r,c))
            res=max(backtrack(r+1,c),backtrack(r-1,c),backtrack(r,c+1),backtrack(r,c-1))
            visit.remove((r,c))
            return grid[r][c] + res
        backtrack(0,0)
        gold=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]!=0:
                    gold=max(gold,backtrack(r,c))
        return gold



