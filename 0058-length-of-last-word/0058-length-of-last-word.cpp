class Solution {
public:
    int lengthOfLastWord(string s) {
        int maxlen = 0, r = s.length() - 1;
        while (s[r] == ' ')
             r--;
        while (r >= 0 && s[r] != ' ')
        {
            maxlen++;
            r--;
        }

        return maxlen;
    }
};