class Solution {
public:
    int scoreOfString(string s) {
        int sum = 0;
        for (int i = 1; i < s.length(); i++)
            sum += abs((int)(s[i-1]) - (int)(s[i]));

        return sum;
    }
};