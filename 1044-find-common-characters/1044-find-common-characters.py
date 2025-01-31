class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_char = Counter(words[0])
        for i in range(1, len(words)):
            curr_char = Counter(words[i])

            for ch in common_char:
                common_char[ch] = min(common_char[ch], curr_char[ch])
        
        print(common_char)
        letters = []
        for key, val in common_char.items():
            for _ in range(val):
                letters.append(key)

        return letters