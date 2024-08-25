class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            nums_row = set()
            nums_col = set()

            for j in range(9):
               # check each row
                num = board[i][j]
                if num in nums_row:
                    return False
                elif num !=".":
                    nums_row.add(num)

               # check each row
                num = board[j][i]
                if num in nums_col:
                    return False
                elif num != ".":
                    nums_col.add(num)
        
        start = [(0,0), (0,3), (0,6),
                 (3,0), (3,3), (3,6),
                 (6,0), (6,3), (6,6)]
        for i, j in start:
            nums = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    num = board[row][col]
                    if num in nums:
                        return False
                    elif num !=".":
                        nums.add(num)
        return True