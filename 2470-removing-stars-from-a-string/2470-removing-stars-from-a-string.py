class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*" and stack:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)