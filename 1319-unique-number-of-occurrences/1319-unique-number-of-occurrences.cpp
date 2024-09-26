class Solution {
public:
    bool uniqueOccurrences(std::vector<int>& arr) {
        std::unordered_map<int, int> count_map;

        // Count occurrences of each number
        for (int num : arr) {
            count_map[num]++;
        }

        std::unordered_set<int> seen_counts;

        // Check if all occurrence counts are unique
        for (const auto& pair : count_map) {
            if (seen_counts.find(pair.second) != seen_counts.end()) {
                return false;
            }
            seen_counts.insert(pair.second);
        }

        return true;
    }
};