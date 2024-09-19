class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n*m: return []
        res = [[0]*n for i in range(m)]
        for k, num in enumerate(original):
            i = k // n
            j = k % n
            res[i][j] = num
        return res