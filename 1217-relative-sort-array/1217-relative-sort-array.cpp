class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> count;
        for (int num : arr1) {
            count[num]++;
        }

        vector<int> out;
        for (int num : arr2) {
            out.insert(out.end(), count[num], num);
            count.erase(num);
        }

        vector<pair<int, int>> remaining(count.begin(), count.end());
        sort(remaining.begin(), remaining.end());

        for (const auto& [num, freq] : remaining) {
            out.insert(out.end(), freq, num);
        }

        return out;
    }
};
