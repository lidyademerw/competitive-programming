class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        def matr(i,j):
            if i>=n or j<0:
                return False
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                return matr(i,j-1)
            else:
                return matr(i+1,j)
        return matr(0,m-1)
        