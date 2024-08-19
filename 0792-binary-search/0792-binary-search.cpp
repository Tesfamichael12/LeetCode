class Solution {
public:
    int search(vector<int>& nums, int target) {
        int L = 0, R = nums.size() - 1;

        while (L <= R){
            int mid = L + (R - L) / 2; // To avoid overflow of integers
            int guess = nums[mid];

            if (guess == target)
                return mid;
            else if (guess > target)
                R = mid - 1;
            else 
                L = mid + 1;
        }
        return -1;
    }
};