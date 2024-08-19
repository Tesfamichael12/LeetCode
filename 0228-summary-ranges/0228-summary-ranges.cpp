class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> out;
        int i = 0;
        while (i < nums.size())
        {
            int start = nums[i];
            while (i < nums.size() - 1 && nums[i] == nums[i + 1] - 1)
                i++;
            
            if (start == nums[i])
                out.push_back(to_string(start));
            else
                out.push_back(to_string(start) + "->" + to_string(nums[i]));
            
            i++;
        }

        return out;
    }
};