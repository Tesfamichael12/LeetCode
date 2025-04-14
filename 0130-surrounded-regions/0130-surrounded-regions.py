class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inbound(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])
        
        dirs = [ (1, 0), (0, 1), (-1, 0), (0, -1) ]

        visited = set()
        def dfs(row, col):
            visited.add((row, col))

            for i, j in dirs:
                r, c = row + i, col + j
                if inbound(r, c) and board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and (i, j):
                    dfs(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited and board[i][j] == "O":
                    print(i, j)
                    board[i][j] = "X"
