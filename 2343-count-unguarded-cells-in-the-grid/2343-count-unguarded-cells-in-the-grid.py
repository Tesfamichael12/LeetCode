class Solution:
    def countUnguarded(self, r: int, c: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * c for _ in range(r)]
        
        for x, y in guards:
            grid[x][y] = "g"
        for x, y in walls:
            grid[x][y] = "w"
        
        count = 0  
        
        for i in range(r):
            # Right 
            j = 0
            while j < c:
                if grid[i][j] == "g":
                    j += 1
                    while j < c and grid[i][j] not in ("w", "g"):
                        if grid[i][j] == "1":
                            j += 1
                            continue
                        grid[i][j] = "1"
                        count += 1
                        j += 1
                else:
                    j += 1
            
            # Left 
            j = c - 1
            while j >= 0:
                if grid[i][j] == "g":
                    j -= 1
                    while j >= 0 and grid[i][j] not in ("w", "g"):
                        if grid[i][j] == "1":
                            j -= 1
                            continue
                        grid[i][j] = "1"
                        count += 1
                        j -= 1
                else:
                    j -= 1

        for j in range(c):
            # Down 
            i = 0
            while i < r:
                if grid[i][j] == "g":
                    i += 1
                    while i < r and grid[i][j] not in ("w", "g"):
                        if grid[i][j] == "1":
                            i += 1
                            continue
                        grid[i][j] = "1"
                        count += 1
                        i += 1
                else:
                    i += 1
            
            # Up 
            i = r - 1
            while i >= 0:
                if grid[i][j] == "g":
                    i -= 1
                    while i >= 0 and grid[i][j] not in ("w", "g"):
                        if grid[i][j] == "1":
                            i -= 1
                            continue
                        grid[i][j] = "1"
                        count += 1
                        i -= 1
                else:
                    i -= 1
        
        res = (r * c)- (count + len(guards) + len(walls))
        
        return res
