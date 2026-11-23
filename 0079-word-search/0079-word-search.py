class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        visit=set()
        def wordser(r,c,i):
            if i==len(word):
                return True
            if r<0 or r>=row or c<0 or c>=col or board[r][c]!=word[i] or (r,c) in visit:
                return False
            visit.add((r,c))
            res=wordser(r+1,c,i+1) or wordser(r-1,c,i+1) or wordser(r,c+1,i+1) or wordser(r,c-1,i+1)
            visit.remove((r,c))
            return res
        for r in range(row):
            for c in range(col):
                if wordser(r,c,0):
                    return True
        return False
         
         