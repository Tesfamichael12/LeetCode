class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map <int, int> hashmap;
        vector<int> res(nums1.size(), -1);

        for (int i = 0; i < nums1.size(); i++)
            hashmap[nums1[i]] = i;
        
        for (int i = 0; i < nums2.size(); i++)
        {
            if (hashmap.count(nums2[i]) > 0)
            {
                for (int j = i + 1; j < nums2.size(); j++)
                {
                    if (nums2[j] > nums2[i])
                    {
                        int k = hashmap[nums2[i]];
                        res[k] = nums2[j];
                        break;
                    }
                }
            }
        }

        return res;
    }
};