class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        # swap vertically
        l, r = 0, n-1
        while l < r:
            m[l], m[r] = m[r], m[l]
            l, r = l+1, r-1
        
        # swap diagonal
        for i in range(n):
            for j in range(i, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]