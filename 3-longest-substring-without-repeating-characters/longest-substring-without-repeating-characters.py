class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        L = R = 0
        hashset = set()
        while R < len(s):
            if s[R] in hashset:
                maxlen = max(maxlen, R - L)
                while s[L] != s[R]:
                    hashset.remove(s[L])
                    L += 1
                L += 1

            hashset.add(s[R])
            R += 1
            maxlen = max(maxlen, R - L)
        
        return maxlen
