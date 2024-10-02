class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        freq = defaultdict(int) # An int dict will return 0 for none existing keys
        maxlen = 0
        for R in range(len(s)):
            freq[s[R]] += 1

            cur_len = R - L + 1
            if cur_len - max(freq.values()) > k:
                freq[s[L]] -= 1
                L += 1
            else:
                maxlen = max(maxlen, cur_len)
        
        return maxlen