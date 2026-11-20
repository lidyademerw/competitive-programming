class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        x=[]
        def genpar(res,open,close):
            if len(res)==2*n:
                x.append(res)
                return
            if open<n:
                genpar(res+"(",open+1,close)
            if close<open:
                genpar(res+")",open,close+1)
        genpar("",0,0)
        return x
        
            
        
        