class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> hashmap;
        for (auto& n : nums)
            hashmap[n]++;

        int maxval = 1, maj = nums[0];
        for (auto& num : hashmap)
        {
            if (num.second > maxval)
            {
                maj = num.first;
                maxval = num.second;
            }
        }
        return maj;
    }
};