class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)
        for ch in ransomNote:
            if ch in hashmap:
                if hashmap[ch] == 0:
                    return False
                else:
                    hashmap[ch]-=1
            else:
                return False
        return True