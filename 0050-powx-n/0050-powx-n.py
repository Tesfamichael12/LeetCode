class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = dict()
        def pow(x, n):
            if (x, n) in memo:
                return memo[(x, n)]
                
            if n == 0:
                return 1

            if n == 1:
                return x
                
            if n % 2 == 0:    
                memo[(x, n)] = pow(x, n // 2) * pow(x, n // 2)
            else:
                memo[(x, n)] = pow(x, n // 2) * pow(x, n // 2 + 1)
            return memo[(x, n)]
        if n > 0:
            return pow(x, n)
        else:
            res = pow(x, -n)
            return 1 / res