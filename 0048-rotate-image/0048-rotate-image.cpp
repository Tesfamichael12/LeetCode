class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        
        // Step 1: Swap rows vertically (reverse the rows)
        int l = 0, r = n - 1;
        while (l < r) {
            swap(matrix[l], matrix[r]);
            l++;
            r--;
        }

        // Step 2: Transpose the matrix by swapping across the diagonal
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {  // Start j from i+1 to avoid redundant swaps
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};
