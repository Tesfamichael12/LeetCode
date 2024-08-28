class Solution {
public:
    void moveZeroes(vector<int>& nums) {
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
    }
};