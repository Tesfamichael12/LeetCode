class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], scores: List[int]) -> int:
        @cache
        def get_score(i):
            return sum(scores[ord(ch) - 97] for ch in words[i])
        
        def backtrack(i, cur_score, chars_available):            
            nonlocal max_score
            for j in range(i, N):
                word_freq = Counter(words[j])
                if all(chars_available[c] >= word_freq[c] for c in word_freq):
                    backtrack(j + 1, cur_score + get_score(j), chars_available - word_freq)
            max_score = max(max_score, cur_score)
        N = len(words)
        max_score = 0
        backtrack(0, 0, Counter(letters))
        return max_score