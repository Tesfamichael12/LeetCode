class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        # first transpose the matrix
        for i in range(n):
            for j in range(i, n): # To avoid redundant swaps, start j from i
                m[i][j], m[j][i] = m[j][i], m[i][j]
                
        # reverse every row
        for i in range(n):
            m[i].reverse()
