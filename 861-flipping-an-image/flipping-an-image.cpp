class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        for (auto& row : image) {
            int l = 0, r = row.size() - 1;
            while (l <= r) {
                // Swap and invert using XOR operation
                int temp = row[l] ^ 1;
                row[l] = row[r] ^ 1;
                row[r] = temp;

                // Move pointers towards the center
                l++;
                r--;
            }
        }
        return image;
    }
};
