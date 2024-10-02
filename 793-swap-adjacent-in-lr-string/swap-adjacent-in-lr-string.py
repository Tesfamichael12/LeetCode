class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s = [[start[i], i] for i in range(len(start)) if start[i] != 'X']
        e = [[end[i], i] for i in range(len(end)) if end[i] != 'X']

        if len(s) != len(e): return False

        for i in range(len(s)):
            if (s[i][0] == 'R' and e[i][0] == 'R'  and s[i][1] > e[i][1]) or (s[i][0] == 'L' and e[i][0] == 'L' and s[i][1] < e[i][1]):
                return False
            elif s[i][0] != e[i][0]:
                return False

        return True 