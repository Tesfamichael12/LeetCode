class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(num):
            if num == 1 or num == 0:
                return 1
            
            return num * fact(num-1)
        
        res = fact(n)

        cnt = 0
        while res:
            if res % 10 == 0:
                cnt += 1
                res //= 10
            else:
                break
            
        return cnt
