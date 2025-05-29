class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bit_masks = [0] * n 

        for i in range(n):
            for c in words[i]:
                bit_masks[i] |= (1 << (ord(c) - ord('a'))) # set bit for the char c
        
        max_len = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (bit_masks[i] & bit_masks[j]):
                    pass
                else:
                    max_len = max(max_len, len(words[i]) * len(words[j]))
        
        return max_len