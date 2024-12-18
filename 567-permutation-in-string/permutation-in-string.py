class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        n = len(s1)
        window = defaultdict(int)

        l = 0
        for r, c in enumerate(s2):
            window[c] += 1

            if r - l + 1 > n:
                if window[s2[l]] == 1:
                    del window[s2[l]]
                else:
                    window[s2[l]] -= 1
                l += 1
            
            if window == target:
                return True

        return False