class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def divide(s, l, r):

            seen = set(s[l:r])

            for i, c in enumerate(s[l:r]):
                if (c.swapcase() not in seen):
                    # split ate c and call both the right and the left

                    left = divide(s, l, l + i)
                    right = divide(s, l + i + 1, r)
                    # print(left, right)

                    if len(left) < len(right):
                        return right
                    else:
                        return left
                
            return s[l:r]
        
        return divide(s, 0, len(s))