class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(a):
            return a == a[::-1]

        count = 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if not (is_palindrome(s[:l] + s[l+1:]) or is_palindrome(s[:r] + s[r+1:])):
                    return False
                else:
                    if is_palindrome(s[:l] + s[l+1:]):
                        l += 1
                    elif is_palindrome(s[:r] + s[r+1:]):
                        r -= 1
                count += 1
                if count > 1:
                    return False
            else:
                l += 1
                r -= 1
        
        return True