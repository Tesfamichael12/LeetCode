class Solution {
public:
   vector<int> intersect(std::vector<int>& nums1,vector<int>& nums2) {
       unordered_map<int, int> count1;
       unordered_map<int, int> count2;
       vector<int> out;

        for (int num : nums1) {
            count1[num]++;
        }

        for (int num : nums2) {
            count2[num]++;
        }

        for (const auto& pair : count1) {
            int num = pair.first;
            if (count2.find(num) != count2.end()) {
                int freq =min(pair.second, count2[num]);
              
                out.insert(out.end(), freq, num);
            }
        }

        return out;
    }
};
