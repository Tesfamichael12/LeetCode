class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> hashset(nums.begin(), nums.end());
        int longest_streak = 0;

        for (int n : hashset) {
            if (hashset.find(n - 1) == hashset.end()) {  // find the start of a sequence 
                int current_num = n;
                int current_streak = 1;

                while (hashset.find(current_num + 1) != hashset.end()) {
                    current_num += 1;
                    current_streak += 1;
                }

                longest_streak = max(longest_streak, current_streak);
            }
        }

        return longest_streak;
    }
};
