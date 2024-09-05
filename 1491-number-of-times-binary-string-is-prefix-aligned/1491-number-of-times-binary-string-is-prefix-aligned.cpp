class Solution {
public:
    int numTimesAllBlue(vector<int>& flips) {
        int max_flipped = 0;
        int count = 0;
        
        for (int i = 0; i < flips.size(); ++i) {
            max_flipped = max(max_flipped, flips[i]);
            if (max_flipped == i + 1) {
                count++;
            }
        }
        
        return count;
    }
};