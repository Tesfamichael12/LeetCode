class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> hashmap;

        for (int i = 0; i < nums.size(); i++)
        {
            if (hashmap.count(target - nums[i]) > 0)
            {
                return {i, hashmap[target - nums[i]]};
            }
            
            hashmap[nums[i]] = i;
        }
        // In c++ even if we are sure to get pair of numbers that satisfy the condition the compiler won't allow to leave the return statement below since the compiler does not guarantee a return statement in all possible execution paths. befor even running the code and see the test cases 
         return {};
    }
};