class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1] # north east south and west
        dy = [1, 0, -1, 0]
        x = y = dir = 0
        maxd = 0
        obstacles = set(map(tuple, obstacles))
        for cmd in commands:
            if cmd == -2:
                dir = (dir-1)%4
            elif cmd == -1:
                dir = (dir+1)%4
            else:
                for _ in range(cmd):
                    if (x + dx[dir], y + dy[dir]) not in obstacles:
                        x += dx[dir]
                        y += dy[dir]
                        maxd = max(maxd, x*x + y*y)
                    else:
                        break
        
        return maxd
                