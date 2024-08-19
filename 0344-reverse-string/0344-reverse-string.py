class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # L, R = 0, len(s) - 1
        # while L < R:
        #     s[L], s[R] = s[R], s[L]
        #     L += 1
        #     R -= 1
        
        s.reverse()