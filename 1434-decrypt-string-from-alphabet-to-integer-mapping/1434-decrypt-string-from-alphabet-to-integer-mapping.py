class Solution:
    def freqAlphabets(self, s: str) -> str:
        s_mapped = ""
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i + 2])
                s_mapped += chr(num + 97 - 1)  
                i += 3  
            else:   
                num = int(s[i])
                s_mapped += chr(num + 97 - 1)  
                i += 1  
        
        return s_mapped
