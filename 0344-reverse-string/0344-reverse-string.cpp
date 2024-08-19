class Solution {
public:
    void reverseString(vector<char>& s) {
        // int L = 0, R = s.size() - 1;
        // while (L < R)
        // {
        //     char temp = s[L];
        //     s[L] = s[R];
        //     s[R] = temp;
        //     L++;
        //     R--;
        // }

        // using the reverse method
        reverse(s.begin(), s.end());
    }
};