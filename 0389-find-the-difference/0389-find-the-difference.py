class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)
        for c in t: 
            if c not in count: 
                return c
            else:
                if count[c] == 1:
                    count.pop(c)
                else:
                    count[c] -= 1