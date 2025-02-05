class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        val = count[s[0]]
        for key in count:
            if count[key] != val:
                return False
        
        return True