class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        
        return 1 + ((num - 1) % 9)