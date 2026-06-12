class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowtrack=[0]*len(matrix)
        columntrack=[0]*len(matrix[0])

        for r in range(len(matrix)):

            for c in range(len(matrix[r])):

                if matrix[r][c]==0:

                    rowtrack[r]=-1
                    columntrack[c]=-1

        for i in range(len(matrix)):

            for j in range(len(matrix[i])):

                if rowtrack[i] ==-1 or columntrack[j]==-1:

                    matrix[i][j]=0





        