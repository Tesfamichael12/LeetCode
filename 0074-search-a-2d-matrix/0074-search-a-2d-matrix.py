class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l, r = 0, (row * col) - 1
        while l <= r:
            mid = (l+r)//2
            i = mid // col
            j = mid % col
            if matrix[i][j] == target:
                return True
            elif target >= matrix[i][j]:
                l = mid + 1
            else:
                r = mid - 1
        return False

