class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [ (1, 0), (0, 1), (-1, 0), (0, -1)]
        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        vis = set()
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    vis.add((i, j))
        time = 0
        while q:
            n = len(q)
            time += 1
            for _ in range(n):
                row, col = q.popleft()

                for i, j in dirs:
                    new_row, new_col = row + i, col + j
                    if inbound(new_row, new_col) and (new_row, new_col) not in vis and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        vis.add((new_row, new_col))
                        q.append((new_row, new_col))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1    
        return time - 1 if time > 0 else time
                    