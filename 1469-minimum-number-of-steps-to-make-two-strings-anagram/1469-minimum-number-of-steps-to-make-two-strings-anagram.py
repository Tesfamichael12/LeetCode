class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        count = 0
        for ch in count_t:
            if ch not in count_s:
                count += count_t[ch]
            else:
                count += abs(count_t[ch] - count_s[ch])

        for ch in count_s:
            if ch not in count_t:
                count += count_s[ch]

        
        return count // 2