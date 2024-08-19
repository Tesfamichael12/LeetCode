class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_map<char, int> s_map; // or simply use a set
        for (char ch : stones)
        {
            if (s_map.count(ch) > 0)
                s_map[ch] ++;
            else
                s_map[ch] = 1;
        }
        int ans = 0;
        for (char c : jewels)
        {
            if (s_map.count(c) > 0)
                ans += s_map[c];
        }
        return ans;
    }
};