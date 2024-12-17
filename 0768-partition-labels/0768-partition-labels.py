class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = i

        size = 0
        end = 0
        res = []

        for i in range(len(s)):
            if hashmap[s[i]] >= i:
                size += 1
                end = max(end, hashmap[s[i]])

            if end == i:
                res.append(size)
                size = 0
        
        return res