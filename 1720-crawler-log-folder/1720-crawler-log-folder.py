class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log[0] != '.':
                stack.append(log)
            else:
                if log == "../" and stack:
                    stack.pop()
        return len(stack)
