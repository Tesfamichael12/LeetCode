class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                s = (i//3, j//3)

                if board[i][j] == ".": continue
                if num in row[i] or num in col[j] or num in square[s]: return False

                row[i].add(num)
                col[j].add(num)
                square[s].add(num)
        return True