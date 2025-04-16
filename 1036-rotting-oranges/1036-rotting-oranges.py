class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [ (1, 0), (0, 1), (-1, 0), (0, -1)]
        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        n, m = len(grid), len(grid[0])
        qu = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    qu.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        print(qu)           
        time = 0
        while qu:
            if fresh == 0: break

            time += 1
            n = len(qu)
            for _ in range(n):
                row, col = qu.popleft()

                for i, j in dirs:
                    new_row, new_col = row + i, col + j
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        qu.append((new_row, new_col))
                        fresh -= 1

        return time if fresh == 0 else -1