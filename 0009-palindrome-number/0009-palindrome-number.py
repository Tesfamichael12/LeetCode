class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        num = x
        rev = 0
        while num:
            rev = rev * 10 + num % 10
            num //= 10
        
        return x == rev