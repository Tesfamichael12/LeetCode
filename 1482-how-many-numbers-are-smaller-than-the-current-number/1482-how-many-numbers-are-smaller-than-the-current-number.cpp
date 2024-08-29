class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        vector<int> result;

        for (int num : nums) {
            int count = lower_bound(sorted_nums.begin(), sorted_nums.end(), num) - sorted_nums.begin();
            result.push_back(count);
        }

        return result;
    }
};
