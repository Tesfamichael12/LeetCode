class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        s.sort(reverse=True)

        for i in range(len(s)-1):
            if s[i] != s[i + 1]:
                s[i] = '0'
        
        s[-1] = '1'

        return "".join(s)