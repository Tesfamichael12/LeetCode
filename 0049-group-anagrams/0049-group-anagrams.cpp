class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagram_map;

        for (const auto& s : strs) {
            string key = s;
            sort(key.begin(), key.end()); 

            anagram_map[key].push_back(s);
        }

        vector<vector<string>> group_anagrams;
        for (const auto& pair : anagram_map) {
            group_anagrams.push_back(pair.second);
        }

        return group_anagrams;
    }
};
