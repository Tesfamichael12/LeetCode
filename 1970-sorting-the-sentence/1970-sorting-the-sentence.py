class Solution:
    def sortSentence(self, s: str) -> str:
        out = ""
        count = {}
        sen = s.split()
        
        for ch in sen:
            count[ch[-1]] = ch[:-1]
        
        new = dict(sorted(count.items())) # if the key is not cased to int it will be a string so we can sort it by this methond i.e count.items() but if it was casted(count[int(ch[:-1])]) we can just sort it by saying new = dict(sorted(count))

        # n = list(new.values())
        # out = " ".join(n)

        for ch in new.values():
            out += (" " + ch)

        return out.strip()      