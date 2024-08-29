class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        unordered_map<int, string> people;
        int n = names.size();

        for (int i = 0; i < n; ++i) {
            people[heights[i]] = names[i];
        }

        sort(heights.begin(), heights.end(), greater<int>());

        vector<string> out;
        for (int height : heights) {
            out.push_back(people[height]);
        }

        return out;
    }
};
