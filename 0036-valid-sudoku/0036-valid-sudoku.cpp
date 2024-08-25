class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Check rows and columns
        for (int i = 0; i < 9; ++i) {
            unordered_set<char> nums_row;
            unordered_set<char> nums_col;

            for (int j = 0; j < 9; ++j) {
                // Check each row
                char num = board[i][j];
                if (nums_row.find(num) != nums_row.end()) {
                    return false;
                } else if (num != '.') {
                    nums_row.insert(num);
                }

                // Check each column
                num = board[j][i];
                if (nums_col.find(num) != nums_col.end()) {
                    return false;
                } else if (num != '.') {
                    nums_col.insert(num);
                }
            }
        }

        // Check 3x3 sub-grids
        vector<pair<int, int>> start = {{0, 0}, {0, 3}, {0, 6}, 
                                        {3, 0}, {3, 3}, {3, 6}, 
                                        {6, 0}, {6, 3}, {6, 6}};
        for (auto [i, j] : start) {
            unordered_set<char> nums;
            for (int row = i; row < i + 3; ++row) {
                for (int col = j; col < j + 3; ++col) {
                    char num = board[row][col];
                    if (nums.find(num) != nums.end()) {
                        return false;
                    } else if (num != '.') {
                        nums.insert(num);
                    }
                }
            }
        }

        return true;
    }
};
