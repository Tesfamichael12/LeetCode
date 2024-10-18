class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashset = set()
        for a in allowed: hashset.add(a)
        print(hashset)
        count = len(words)
        for s in words:
            for c in s:
                if c not in hashset:
                    count -= 1
                    break
            
        return count