class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n = nums.size();
        int max1 = 0;  
        int l = 0;    

        for (int r = 0; r < n; ++r) { 
            if (nums[r] == 0) {
                l = r + 1;
            } else {
                max1 = max(max1, r - l + 1);
            }
        }

        return max1;
    }
};