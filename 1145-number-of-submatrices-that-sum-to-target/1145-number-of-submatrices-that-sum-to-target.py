class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        rows, cols = len(mat), len(mat[0])
        # append trailling zeros for negative indeces
        mat.append([0]*cols)
        for row in mat:
            row.append(0)
        
        # build a 2D prifix sum 
        for i in range(rows):
            for j in range(cols):
                mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
        
        # count the sub-matrices which sum to target
        # Iterate through all possible pairs of columns
        cnt = 0
        for col1 in range(cols):
            for col2 in range(col1, cols):
                # Use a hashmap to count the number of subarrays with a given sum
                seen = {0: 1}
                current_sum = 0
                for row in range(rows):
                    cur = mat[row][col2] - mat[row][col1 - 1]
                    key = cur - target

                    if key in seen:
                        cnt += seen[key]
                    if cur in seen:
                        seen[cur] += 1
                    else:
                        seen[cur] = 1
        
        return cnt
