class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res(nums.size());
        int l = 0, r = nums.size() - 1;
        int i = nums.size() - 1;
        
        while (l <= r) {
            int leftSquare = nums[l] * nums[l];
            int rightSquare = nums[r] * nums[r];
            
            if (leftSquare > rightSquare) {
                res[i] = leftSquare;
                l++;
            } else {
                res[i] = rightSquare;
                r--;
            }
            i--;
        }
        
        return res;
    }
};