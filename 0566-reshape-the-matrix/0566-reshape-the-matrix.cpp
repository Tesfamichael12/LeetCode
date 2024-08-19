class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int R = mat.size(), C = mat[0].size();
        int size = R * C;

        if (size != r * c || (R == r && C == c))
            return mat;

        vector<vector<int>> reshaped(r, vector<int>(c));
        vector <int> mat_liner(size);

        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
            {
                mat_liner[(C * i) + j] = mat[i][j];
            }
        }

        for (int i = 0; i < size; i++)
        {
            reshaped[i / c][i % c] = mat_liner[i];
        }
        
        return reshaped;
    }
};