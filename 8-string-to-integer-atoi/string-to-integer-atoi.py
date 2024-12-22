class Solution:
    def myAtoi(self, s: str) -> int:
        trimed = s.strip()
        if not trimed:
            return 0
        
        sign = -1 if trimed[0] == '-' else 1
        num = 0
        i = 0
        if trimed[0] in ['-', '+']:
            i += 1

        while i < len(trimed) and trimed[i].isnumeric():
            num = num * 10 + int(trimed[i])
            i += 1

        num *= sign
        if num > 2 ** 31 - 1: return 2 ** 31 - 1
        elif num < -1 * 2 **31: return -1 * 2 ** 31

        return num
