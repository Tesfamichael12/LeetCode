class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        reshaped = [[0] * c for _ in range(r)] # initialize a 2D array
        size = len(mat) * len(mat[0])
        mat_liner = []

        if size != r * c or (len(mat) == r and len(mat[0]) == c):
            return mat
        
        for n in mat:
            mat_liner.extend(n)

        for i in range(size):
            reshaped[i // c][i % c] = mat_liner[i]

        return reshaped
