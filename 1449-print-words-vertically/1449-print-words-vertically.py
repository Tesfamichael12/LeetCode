class Solution:
    def printVertically(self, s: str) -> List[str]:
        sm = s.split()
        max_len = max(len(word) for word in sm)  
        
        res = []
        
        for i in range(max_len):
            ch = []
            for word in sm:
                if i < len(word):
                    ch.append(word[i])  
                else:
                    ch.append(" ")  
            
            res.append("".join(ch).rstrip())
        
        return res
