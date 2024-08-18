class Solution {
public:
    bool isPalindrome(string s) {
        int L = 0, R = s.length() - 1;

        while (L < R)
        {
            if (L < R && !(isalpha(s[L]) || isdigit(s[L]))) // or isalnum(s[L])
            {
                L++;
                continue;
            }
            if (L < R && !(isalpha(s[R]) || isdigit(s[R])))
            {
                R--;
                continue;

            }
            if (tolower(s[L]) != tolower(s[R]))
               return false;
            L++, R--;
        }
        return true;
    }
};