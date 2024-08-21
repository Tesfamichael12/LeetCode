class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {'b': 0, 'a' : 0, 'l' : 0, 'o' : 0, 'n': 0}
        for c in text:
            if c in balloon:
                balloon[c] += 1 
            else: continue
        
        valid = balloon['b']
        for n in "balloon":
            if n == 'l' or n == 'o':
                valid = min(valid, balloon[n] // 2)
            else:
                valid = min(valid, balloon[n])
        
        return valid

