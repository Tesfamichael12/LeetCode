class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find the location of the Rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    row, col = i, j
                    break

        print(row, col)
        
        # search for avaliable pawns to capture
        count = 0
        i, j = row, col 
        while i > 0:
            i -= 1
            if board[i][j] == 'B':
                break
            if board[i][j] == 'p':
                count += 1
                break

        i, j = row, col 
        while i < 7:
            i += 1
            if board[i][j] == 'B':
                break
            if board[i][j] == 'p':
                count += 1
                break

        i, j = row, col 
        while j > 0:
            j -= 1
            if board[i][j] == 'B':
                break
            if board[i][j] == 'p':
                count += 1
                break

        i, j = row, col 
        while j < 7:
            j += 1
            if board[i][j] == 'B':
                break
            if board[i][j] == 'p':
                count += 1
                break

        return count
        