class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        L, R = 0, 0 
        while L < len(s) and R < len(t):
            if s[L] == t[R]:
                L += 1
            R += 1
        
        return True if L == len(s) else False