class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if len(original) != n*m: return res
        a, b = 0, n
        for i in range(m):
            res.append(original[a:b])
            a += n
            b += n
        return res