class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 1, x
        ans = 0
        while L <= R:
            mid = (L+R)//2
            g = mid * mid
            if g <= x:
                ans = mid
                L = mid + 1
            else:
                R = mid - 1
        return ans
