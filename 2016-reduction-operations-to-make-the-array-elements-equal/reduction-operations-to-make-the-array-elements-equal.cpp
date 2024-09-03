class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        int op = 0, cur = 0;
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i-1] < nums[i]) cur += 1;
            op += cur;
        }
        return op;
    }
};