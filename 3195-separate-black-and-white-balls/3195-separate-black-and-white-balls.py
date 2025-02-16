class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        cnt = 0
        cnt_0 = s.count('1')
        l, r = 0, len(s) - cnt_0

        while r < len(s):
            while l < r and s[l] == '0':
                l += 1
            
            while r < len(s) and s[r] == '1':
                r += 1
            
            if r == len(s): break
            cnt += (r - l)
            r += 1
            l += 1

        return cnt