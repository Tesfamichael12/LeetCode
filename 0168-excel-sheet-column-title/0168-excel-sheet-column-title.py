class Solution:
    def convertToTitle(self, num: int) -> str:
        res = []
        while num:
            num -= 1
            ch = chr(num % 26 + ord('A'))
            res.append(ch)
            num //= 26
        res.reverse()

        return "".join(res)
