class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x *= -1

        reverse = 0
        while True:
            if x <= 0: break

            rev = x % 10
            reverse = reverse * 10 + rev
            x //= 10
        if reverse > 2 ** 31 - 1:
            return 0
            
        if isNegative:
            return (-1 * reverse)
        else:
            return reverse
        