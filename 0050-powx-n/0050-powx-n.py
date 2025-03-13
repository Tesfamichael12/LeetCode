class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0: return 1

            half = pow(x, n // 2)

            if n % 2:
                return x * half * half
            else:
                return half * half
        
        if n > 0:
            return pow(x, n)
        else:
            return 1 / pow(x, abs(n))