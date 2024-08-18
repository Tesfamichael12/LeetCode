class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> hashset;

        for (auto& num : nums)
        {
            if (hashset.count(num) == 1)
               return true;
            else
               hashset.insert(num);
        }
        return false;
    }
};