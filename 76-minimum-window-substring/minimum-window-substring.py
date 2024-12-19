from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = defaultdict(int)
        minsub = ""
        l = 0
        valid_count = 0  # Tracks how many characters in the window meet the target requirements

        for r in range(len(s)):
            char = s[r]
            if char in target:
                window[char] += 1
                if window[char] == target[char]:
                    valid_count += 1

            # When all target characters are satisfied, try shrinking the window
            while valid_count == len(target):
                if not minsub or len(minsub) > r - l + 1:
                    minsub = s[l:r+1]

                # Shrink the window from the left
                if s[l] in target:
                    window[s[l]] -= 1
                    if window[s[l]] < target[s[l]]:
                        valid_count -= 1
                l += 1

        return minsub
