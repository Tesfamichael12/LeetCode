class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]  # North, East, South, West
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        maxd = 0

        for cmd in commands:
            if cmd == -2:  # Turn left
                di = (di - 1) % 4
            elif cmd == -1:  # Turn right
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        maxd = max(maxd, x*x + y*y)
                    else:
                        break

        return maxd