class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while res % 10 != res:
            sum = 0
            while True:
                sum += res % 10
                res //= 10
                
                if res <= 0:
                    break
            
            res = sum
        return res