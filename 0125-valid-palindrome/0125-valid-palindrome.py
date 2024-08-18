class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L <= R:
            if not s[L].isalnum(): # if it is not both alphabetic nor numeric use the method isalnum() or use isalpha() and isnumeric() or isdigit() together
                L += 1
                continue
            if not s[R].isalnum():
                R -= 1
                continue
            if (s[L].lower()) != (s[R].lower()):
                return False
            L += 1
            R -= 1
        
        return True