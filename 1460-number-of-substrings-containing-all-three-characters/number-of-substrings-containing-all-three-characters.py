class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {c:0 for c in 'abc'}
        L = res = 0
        for R in range(len(s)):
            count[s[R]] += 1

            while all(count.values()): # count['a'] > 0 and count['b'] and count['c']
                res += len(s) - R
                count[s[L]] -= 1
                L += 1
        
        return res