class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i - 1] == nums[i])
            {
                nums[i - 1] *= 2;
                nums[i] = 0;
            }
        }

        int l = 0, r = 1;
        while (r < nums.size())
        {
            if (nums[l] == 0 && nums[r] != 0)
            {
                // swap using XOR handy trick, without temp variable i.e without extra space
                nums[l] ^= nums[r]; // Step 1
                nums[r] ^= nums[l]; // Step 2
                nums[l] ^= nums[r]; // Step 3
                l++;
            }
            else if (nums[l] != 0)
                l++;
            r++;
        }

        return nums;
    }
};