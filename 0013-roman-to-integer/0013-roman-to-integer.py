class Solution:
    def romanToInt(self, s: str) -> int:
        symbolVal = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        num = 0
        i = len(s) - 1
        while i >= 0:
            if i > 0 and symbolVal[s[i]] > symbolVal[s[i - 1]]:
                num += (symbolVal[s[i]] - symbolVal[s[i - 1]])
                i -= 2
            else:
                num += symbolVal[s[i]]
                i -= 1
        return num

# NOTE
'''
we should use a while loop, if we were to use for loop we wouldn't be able to update i manualy since it get updated by the for loop automatically the for loop won't allow us to update it 
'''