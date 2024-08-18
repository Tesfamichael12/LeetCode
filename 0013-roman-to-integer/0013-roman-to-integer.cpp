class Solution {
public:
    int romanToInt(string s) {
            unordered_map<char, int> symbolVal = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int num = 0, i = s.length() - 1;
        while (i >= 0)
        {
            if (i > 0 && symbolVal[s[i]] > symbolVal[s[i - 1]]){
                num += (symbolVal[s[i]] - symbolVal[s[i - 1]]);
                i-=2;
            }
            else
            {
               num += symbolVal[s[i]]; 
               i--;
            }

        }
        return num;
    }
};