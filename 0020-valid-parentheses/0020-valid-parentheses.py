class Solution:
    def isValid(self, s: str) -> bool:
        par = { ']' :'[' ,  ')' : '(', '}' : '{' }

        stack = []
        for c in s:
            if c in par:
                if len(stack) == 0 or stack[-1] != par[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0
