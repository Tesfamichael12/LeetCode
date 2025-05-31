class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        state = [] # holds the current state of the sub-array i.e even or odd number of the vowels 
        for c in s:
            if c in vowels:
                mask ^= (1 << (ord(c) - ord('a')))
            
            state.append(mask)
        
        # print(state)

        max_len = 0
        seen = {0:-1}
        for i, mask in enumerate(state):
            
            if mask in seen:
                max_len = max(max_len, i - seen[mask])
            else:
                seen[mask] = i

        return max_len

