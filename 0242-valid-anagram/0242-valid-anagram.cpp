class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;

        unordered_map <char, int> map1;
        unordered_map <char, int> map2;

        for (char s : s)
            map1[s]++;
        
        for (char t : t)
            map2[t]++;

        return (map1 == map2);

    }
};