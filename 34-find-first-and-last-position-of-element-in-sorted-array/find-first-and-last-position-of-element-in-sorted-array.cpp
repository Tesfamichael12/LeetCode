class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto lb = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        if (lb >= nums.size() || nums[lb] != target)
            return {-1, -1};
        auto ub = upper_bound(nums.begin(), nums.end(), target) - nums.begin();
        return {(int)lb, (int)ub-1};
    }
};