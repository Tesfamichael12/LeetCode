class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def is_in_row(word, row):
            word = word.lower()
            if word[0] in row:
                for ch in word:
                    if ch not in row:
                        return False
            else:
                return False

            return True
                    
        top = set("qwertyuiop")
        mid = set("asdfghjkl")
        bottom = set("zxcvbnm")

        res = []
        for word in words:
            if word[0].lower() in top and is_in_row(word, top):
                res.append(word)
            if word[0].lower() in mid and is_in_row(word, mid):
                res.append(word)
            if word[0].lower() in bottom and is_in_row(word, bottom):
                res.append(word)

        return res
                