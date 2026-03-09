class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri=[[1]]
        for i in range(rowIndex):
            pre=tri[-1]
            x=[1]
            for j in range(len(pre)-1):
                x.append(pre[j]+pre[j+1])
            x.append(1)
            tri.append(x)
        return tri[rowIndex]

        
        