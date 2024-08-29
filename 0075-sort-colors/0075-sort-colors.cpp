class Solution {
public:
    void sortColors(vector<int>& nums) {

        unordered_map<int, int> hashmap;
        for (int i = 0; i < nums.size(); i++)
        {
            if (hashmap.count(nums[i]) > 0)
                hashmap[nums[i]]++;
            else
                hashmap[nums[i]] = 1;
        }

        int k = 0;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < hashmap[i]; j++)
            {
                nums[k++] = i;
            }
        }
    }
};