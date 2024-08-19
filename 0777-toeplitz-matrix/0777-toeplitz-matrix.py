class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
        return True