class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // Sort by the first element of each interval
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        int i = 1;
        while (i < intervals.size()) {
            if (intervals[i-1][1] >= intervals[i][0]) {
                intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1]);
                intervals.erase(intervals.begin() + i);
            } else {
                i++;
            }
        }
        return intervals;
    }
};
