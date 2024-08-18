class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        int i = 0, d = 1;
        vector<string> rows(numRows);

        for (char c : s) {
            rows[i] += c;
            if (i == 0) {
                d = 1;
            } else if (i == numRows - 1) {
                d = -1;
            }
            i += d;
        }

        string res = "";
        for (const string& row : rows) {
            res += row;
        }

        return res;
    }
};
