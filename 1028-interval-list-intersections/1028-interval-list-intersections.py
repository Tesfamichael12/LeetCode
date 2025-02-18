class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0

        while i < len(f) and j < len(s):
            x = max(f[i][0], s[j][0])
            y = min(f[i][1], s[j][1])

            if y - x >= 0:
                res.append([x, y])

            if f[i][1] < s[j][1]:
                i += 1
            else:
                j += 1
            
        return res


