class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for s in strs:
            key = tuple(sorted(s))
            
            if key in anagram_dict:
                anagram_dict[key].append(s)
            else:
                anagram_dict[key] = [s]

        group_anagrams = list(anagram_dict.values())
        return group_anagrams
