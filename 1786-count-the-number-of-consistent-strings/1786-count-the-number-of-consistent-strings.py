class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allow = Counter(allowed)
        for word in words:
            flag = True
            for c in word:
                if c not in allow:
                    flag = False
            if flag:
                count += 1
        
        return count