class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(2 * last, 1)
        
        return stack[0]