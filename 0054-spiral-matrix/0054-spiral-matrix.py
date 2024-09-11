class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []      
        x, y = len(matrix), len(matrix[0])
        top, bottom = 0, x - 1
        left, right = 0, y - 1

        while top <= bottom and left <= right:
            # Traverse from left to right
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            
            # Traverse down the right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # Traverse upwards along the left column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
