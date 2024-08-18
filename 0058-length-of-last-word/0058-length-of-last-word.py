class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        maxlen = 0
        r = len(s) - 1
        while s[r] == ' ':
            r -= 1
        
        while r >= 0 and s[r] != ' ':
            maxlen += 1
            r -= 1

        return maxlen