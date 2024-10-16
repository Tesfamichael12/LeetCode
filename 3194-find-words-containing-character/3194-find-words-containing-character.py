class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if x in w:
                res.append(i)
        return res