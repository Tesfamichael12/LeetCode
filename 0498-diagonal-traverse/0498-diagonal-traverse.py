class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)

        row = len(matrix)
        col = len(matrix[0])

        x, y = 0, 0
        while True:
            i, j = x, y
            while i >= 0 and j < col:
                key = i + j
                diagonal[key].append(matrix[i][j])
                i -= 1
                j += 1
            
            if key % 2 != 0:
                diagonal[key].reverse()
            
            # update the start pos
            if x != row - 1:
                x += 1
            else:
                y += 1
            
            if y == col: break

        res = []
        for val in diagonal.values():
            res.extend(val)
        
        return res