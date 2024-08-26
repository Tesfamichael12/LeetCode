class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        // we should use double insted of float since we want precision
        double maxave = -INFINITY; // using the cmath library, for double type we use can use INFINITY but for very big numbers useHUGE_VAL
        double ave = -INFINITY;
        int sum = 0;
        int l = 0, r = 0;
        while (r < nums.size())
        {
            while (r - l < k)
            {
                sum += nums[r];
                r++;
            }
            ave = (double) sum / k;
            // cout << fixed << setprecision(5);
            ave = round(ave * 100000.0) / 100000.0;
            maxave = max(maxave, ave);
            sum -= nums[l];
            l++;
        }
        return maxave;
    }
};