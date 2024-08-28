class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9), cols(9);
        vector<unordered_set<char>> subgrids(9);

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') continue; 

                char num = board[i][j];
                int subgridIndex = (i / 3) * 3 + (j / 3);

                if (rows[i].count(num) || cols[j].count(num) || subgrids[subgridIndex].count(num)) {
                    return false;
                }

                rows[i].insert(num);
                cols[j].insert(num);
                subgrids[subgridIndex].insert(num);
            }
        }
        return true;
    }
};
