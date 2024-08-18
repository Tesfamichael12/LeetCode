class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int L = 0, R = nums.size() - 1;

        while (L <= R) {
            int mid = L + (R - L) / 2;  // This avoids any potential overflow

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                R = mid - 1;
            } else {
                L = mid + 1;
            }
        }

        return L;
    }
};