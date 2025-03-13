class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7 

        def mod_pow(b, e):
            if e == 0: return 1

            if e % 2:
                return b % mod * ((mod_pow(b, e // 2) % mod )**2) % mod
            else:
                return ((mod_pow(b, e // 2) % mod)**2) % mod
    
        even = 5
        prime = 4

        odd_i = n // 2
        even_i = n - odd_i
        # the built in function pow will cause TL so use a custome mod_pow function
        # return (pow(even, even_i) * pow(prime, odd_i)) % mod 
        res = (mod_pow(even, even_i) * mod_pow(prime, odd_i)) % mod

        return res