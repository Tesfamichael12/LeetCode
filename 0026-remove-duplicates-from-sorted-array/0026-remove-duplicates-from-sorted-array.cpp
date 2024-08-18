class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = 1, r = 1;
        while (r < nums.size())
        {
            if (nums[r] != nums[r - 1])
            {
                nums[l] = nums[r];
                l++;
            }
            r++;
        }

        return l;
    }
};