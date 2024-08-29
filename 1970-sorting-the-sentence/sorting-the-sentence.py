class Solution:
    def sortSentence(self, s: str) -> str:
        out = ""
        count = {}
        sen = s.split()
        
        for ch in sen:
            count[ch[-1]] = ch[:-1]
        
        new = dict(sorted(count.items()))
        print(new)

        n = list(new.values())
        out = " ".join(n)

        return out.strip()      