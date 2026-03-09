class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return [[]]
        tri=[[1]]
        for i in range(numRows-1):
            pre=tri[-1]#[1]
            x=[1]
            for j in range(len(pre)-1):
                x.append(pre[j] + pre[j+1])
            x.append(1)
            tri.append(x)
        return tri



        