from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        window = defaultdict(int)
        res = []
        n = len(p)
        L = 0

        for R in range(len(s)):
            window[s[R]] += 1

            if R - L + 1 > n:
                if window[s[L]] == 1:
                    del window[s[L]]
                else:
                    window[s[L]] -= 1
                L += 1

            if window == target:
                res.append(L)

        return res