class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            anagram_dict[key].append(s)

        return anagram_dict.values()
