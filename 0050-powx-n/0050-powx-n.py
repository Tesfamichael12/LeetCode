class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def pow(x,n):
            if n < 1: return 1
            if n == 1: return x

            if n % 2 == 0:
                return pow(x, n // 2) * pow(x, n // 2)
            else:
                return pow(x, n // 2) * pow(x, n // 2 + 1)
            
        
        res = pow(x, abs(n))

        if n < 0:
            return 1 / res
        
        return res