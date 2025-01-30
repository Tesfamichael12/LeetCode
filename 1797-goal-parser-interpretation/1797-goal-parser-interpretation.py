class Solution:
    def interpret(self, command: str) -> str:
        message = []
        for i in range(len(command)):
            if command[i] == 'G':
                message.append("G")
            elif i < len(command) and command[i] == '(' and command[i+1] == ')':
                message.append('o')
                i += 1
            elif i < len(command) and command[i] == '(' and command[i+1] == 'a':
                message.append('al')
                i += 2
        
        return "".join(message)