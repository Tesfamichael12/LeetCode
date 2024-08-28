class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        s = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue

                num = board[i][j]
                # checking the rows
                if num in row[i]:
                    return False
                else:
                    row[i].add(num)

                # check the cols
                if num in col[j]:
                    return False
                else:
                    col[j].add(num)

                # check the squares
                if num in s[i//3, j//3]:
                    return False
                else:
                    s[i//3, j//3].add(num)
        return True


                