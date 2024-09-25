class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        freq = collections.defaultdict(int)

        for word in words:
            hashword = frozenset(word)
            count += freq[hashword]
            freq[hashword] += 1
        return count
