class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size();
        int max_w = 0, z = 0, l =0;

        for (int r = 0; r < n; r++)
        {
            if (nums[r] == 0)
                z++;

            while (z > k)
            {
                if (nums[l] == 0)
                    z--;
                l++;
            }
            int w = r - l + 1;
            max_w = max(max_w, w);
        }
        return max_w;
    }
};