class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1 :
            return target in matrix[0]
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        if len(matrix[0]) == 1:
            l , r = 0 , len(matrix)-1
            while l <= r:
                mid = (l + r) // 2
                if matrix[mid][0] == target:
                    return True
                elif matrix[mid][0] > target :
                    r = mid - 1
                else:
                    l = mid + 1
        for i in matrix:
            l , r = 0 , len(i)  - 1
            if target >= i[l] and target <= i[r]:
                while l <= r:
                    mid = (l + r) // 2
                    if target == i[mid]:
                        return True
                    elif target < i[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
        return False
