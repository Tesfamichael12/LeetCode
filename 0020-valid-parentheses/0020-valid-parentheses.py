class Solution:
    def isValid(self, s: str) -> bool:
        pr_dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        for p in s:
            if p in pr_dict.values():
                stack.append(p)
            elif stack and stack[-1] == pr_dict[p]:
                stack.pop()
            else: # if stack is empty but p is in pr_dict.keys() i.e we have extra closing brace
                return False

        return stack == []