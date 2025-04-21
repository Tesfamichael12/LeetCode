class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        qu = deque()
        qu.append("0000")
        visited = set()
        moves = 0
        while qu:
            for _ in range(len(qu)):
                
                cur_guess = qu.popleft()
                if cur_guess in visited or cur_guess in deadends:
                    continue
                if cur_guess == target:
                    return moves

                visited.add(cur_guess)
                for i in range(4):
                    digit = int(cur_guess[i])
                    for diff in [-1, 1]:
                        new_digit = (digit + diff) % 10
                        new_guess = cur_guess[:i] + str(new_digit) + cur_guess[i+1:]
                        qu.append(new_guess)

            moves += 1
        
        return -1